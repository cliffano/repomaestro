<img align="right" src="https://raw.github.com/cliffano/repomaestro/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/repomaestro/workflows/CI/badge.svg)](https://github.com/cliffano/repomaestro/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/repomaestro/badge.svg)](https://snyk.io/test/github/cliffano/repomaestro)
[![Dependencies Status](https://img.shields.io/librariesio/release/pypi/repomaestro)](https://libraries.io/github/cliffano/repomaestro)
[![Published Version](https://img.shields.io/pypi/v/repomaestro.svg)](https://pypi.python.org/pypi/repomaestro)
<br/>

Repo Maestro
------------

Repo Maestro is a file generator using code repositories data rendered with a Jinja2 template.

Installation
------------

    pip3 install repomaestro

Usage
-----

Initialise a Repo Maestro configuration file with GitHub repositories:

    GITHUB_TOKEN=<github_token> repomaestro init --conf-file .repomaestro.yaml --github-id cliffano

Please note that the fetched GitHub repositories are based on the ones accessible by the provided `GITHUB_TOKEN`, which can include repositories owned by multiple users and orgs.

When `--github-id` flag is provided, only the repositories owned by the specified user or org will be included in Repo Maestro configuration file.

Generate output file based on a Jinja2 template:

    repomaestro gen --conf-file .repomaestro.yaml --template-file some-template.j2 --out-file some-output.json

Show help guide:

    repomaestro --help

Colophon
--------

[Developer's Guide](https://cliffano.github.io/developers_guide.html#python)

Build reports:

* [Lint report](https://cliffano.github.io/repomaestro/lint/pylint/index.html)
* [Code complexity report](https://cliffano.github.io/repomaestro/complexity/wily/index.html)
* [Unit tests report](https://cliffano.github.io/repomaestro/test/pytest/index.html)
* [Test coverage report](https://cliffano.github.io/repomaestro/coverage/coverage/index.html)
* [Integration tests report](https://cliffano.github.io/repomaestro/test-integration/pytest/index.html)
* [API Documentation](https://cliffano.github.io/repomaestro/doc/sphinx/index.html)
