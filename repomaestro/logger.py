"""Logger for Repo Maestro."""

from conflog import Conflog


def init():
    """Initialize logger."""

    cfl = Conflog(
        conf_dict={"level": "info", "format": "[repomaestro] %(levelname)s %(message)s"}
    )
    cfl.close_logger_handlers(__name__)

    return cfl.get_logger(__name__)
