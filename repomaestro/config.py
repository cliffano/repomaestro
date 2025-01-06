"""Configuration loader.
"""

import yaml
from .logger import init


def read(conf_file: str) -> dict:
    """Read configuration values from file."""

    logger = init()
    logger.info(f"Reading configuration file {conf_file} ...")

    conf = {}
    with open(conf_file, "r", encoding="utf-8") as stream:
        conf = yaml.safe_load(stream)

    return conf


def write(conf_file: str, conf: dict) -> None:
    """Write configuration values to file."""

    logger = init()
    logger.info(f"Writing configuration file {conf_file} ...")

    with open(conf_file, "w", encoding="utf-8") as stream:
        yaml.dump(conf, stream, default_flow_style=False)
