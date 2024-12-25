# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import logging
import unittest
from repomaestro.logger import init


class TestLogger(unittest.TestCase):

    def test_init(self):

        logger = init()
        assert isinstance(logger, logging.LoggerAdapter) is True
