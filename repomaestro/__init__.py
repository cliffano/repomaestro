# pylint: disable=too-many-locals
"""
Repo Maestro
============
File generator using code repositories data rendered with a Jinja2 template.
"""
import os
import click
from jinja2 import Environment, FileSystemLoader
from .config import read as read_config, write as write_config
from .logger import init as init_logger
from .platform.github import get_repos_data as get_github_repos_data

DEFAULT_CONF_FILE = f'{os.environ["HOME"]}/.repomaestro.yaml'


def init_config(conf_file: str, github_token: str, github_ids: list) -> None:
    """Initialise Repo Maestro configuration from SCM platforms"""

    logger = init_logger()
    repos_data = {}

    if github_ids != []:

        logger.info("Retrieving repos data from GitHub...")
        github_repos_data = get_github_repos_data(github_token, github_ids)
        repos_data.update(github_repos_data)

        if repos_data:
            write_config(conf_file, repos_data)
            logger.info(f"Repo Maestro configuration written to {conf_file}")

    else:
        logger.warning("Skipping configuration initialisation. No GitHub ID provided.")


def gen_file(
    conf_file: str,
    template_file: str,
    out_file: str,
    include_keywords_list: list,
    exclude_keywords_list: list,
) -> None:
    """Generate an output file using Repo Maestro data rendered with a Jinja2 template file"""

    logger = init_logger()
    params = read_config(conf_file)

    if include_keywords_list:
        params = {
            k: v
            for k, v in params.items()
            if all(x in v["keywords"] for x in include_keywords_list)
            and not any(x in v["keywords"] for x in exclude_keywords_list)
        }

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_file)
    content = template.render({"repos": params})

    with open(out_file, "w", encoding="utf-8") as output_stream:
        output_stream.write(content)
    logger.info(f"Generated output file written to {out_file}")


@click.command()
@click.option(
    "--conf-file",
    show_default=True,
    default=DEFAULT_CONF_FILE,
    type=str,
    help="Repo Maestro configuration file",
)
@click.option(
    "--github-ids", show_default=False, type=str, help="Comma-separated GitHub IDs"
)
def init(conf_file: str, github_ids: str) -> None:
    """Initialise Repo Maestro configuration file"""
    conf_file = conf_file if conf_file else DEFAULT_CONF_FILE
    github_token = os.getenv("GITHUB_TOKEN")
    github_ids_list = github_ids.split(",") if github_ids else []
    init_config(conf_file, github_token, github_ids_list)


@click.command()
@click.option(
    "--conf-file",
    show_default=True,
    default=DEFAULT_CONF_FILE,
    type=str,
    help="Repo Maestro configuration file",
)
@click.option(
    "--template-file",
    show_default=False,
    type=str,
    help="Jinja2 template file",
)
@click.option(
    "--include-keywords",
    show_default=False,
    type=str,
    help="Comma-separated list keywords of repositories to be included",
)
@click.option(
    "--exclude-keywords",
    show_default=False,
    type=str,
    help="Comma-separated list keywords of repositories to be excluded",
)
@click.option("--out-file", show_default=False, type=str, help="Output file")
def gen(
    conf_file: str,
    template_file: str,
    include_keywords: str,
    exclude_keywords: str,
    out_file: str,
) -> None:
    """Generate output file from repositories data in Repo Maestro configuration file"""
    conf_file = conf_file if conf_file else DEFAULT_CONF_FILE
    include_keywords_list = include_keywords.split(",") if include_keywords else []
    exclude_keywords_list = exclude_keywords.split(",") if exclude_keywords else []
    gen_file(
        conf_file, template_file, out_file, include_keywords_list, exclude_keywords_list
    )


@click.group()
def cli():
    """Repo Maestro CLI"""


cli.add_command(init)
cli.add_command(gen)
