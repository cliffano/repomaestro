# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from click.testing import CliRunner
from repomaestro import cli


class TestCli(unittest.TestCase):

    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage: cli [OPTIONS]", result.output)
        self.assertIn("Show this message and exit.", result.output)
