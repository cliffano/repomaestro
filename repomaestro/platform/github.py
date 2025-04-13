# pylint: disable=too-many-locals
"""
GitHub repositories data fetcher.
"""
from github import Github
from github import Auth
from ..logger import init


def get_repos_data(github_token: str, github_ids: list) -> dict:
    """Fetch repositories data from GitHub.
    All repositories that GitHub token has access to will be fetched.
    When one or more GitHub IDs is provided, the repositories will be
    filtered to exclude repositories which are not owned by any of
    the provided GitHub IDs.
    """

    logger = init()

    auth = Auth.Token(github_token)
    g = Github(auth=auth)

    data = {}
    for repo in g.get_user().get_repos():
        if github_ids == [] or repo.owner.login in github_ids:
            logger.info(f"- {repo.name}")
            # Complete list of PyGithub Repository:
            # https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html
            data[repo.name] = {
                "homepage": repo.homepage,
                "keywords": repo.topics,
                "git_url": repo.git_url,
                "ssh_url": repo.ssh_url,
            }
        else:
            logger.info(f"- {repo.name} (skipped)")

    g.close()

    return data
