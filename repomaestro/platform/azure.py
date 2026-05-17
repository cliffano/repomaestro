"""
Azure DevOps repositories data fetcher.
"""

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from ..logger import init


def get_repos_data(azure_token: str, azure_ids: list, azure_projects: list) -> dict:
    """Fetch repositories data from Azure DevOps.
    Expects Azure DevOps organisation IDs (org names) and an Azure PAT.
    Optionally filters to a set of project names. Repositories are grouped by
    project to avoid name collisions across projects.
    """

    logger = init()

    data = {}
    for org in azure_ids:
        base_url = f"https://dev.azure.com/{org}"
        logger.info(f"Retrieving repos data from Azure DevOps org {org} ...")

        credentials = BasicAuthentication("", azure_token)
        connection = Connection(base_url=base_url, creds=credentials)

        core_client = connection.clients.get_core_client()
        git_client = connection.clients.get_git_client()

        continuation_token = None
        while True:
            projects_response = core_client.get_projects(
                continuation_token=continuation_token
            )

            for project in projects_response.value:
                if azure_projects and project.name not in azure_projects:
                    logger.info(f"- {project.name} (skipped)")
                    continue

                repos = git_client.get_repositories(project.id)
                for repo in repos:
                    repo_key = f"{project.name}/{repo.name}"
                    logger.info(f"- {repo_key}")
                    data[repo_key] = {
                        "homepage": repo.web_url,
                        "keywords": [
                            "provider:azure",
                            f"org:{org}",
                            f"project:{project.name}",
                        ],
                        "git_url": repo.remote_url,
                        "ssh_url": repo.ssh_url,
                    }

            continuation_token = projects_response.continuation_token
            if not continuation_token:
                break

    return data
