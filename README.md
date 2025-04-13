<img align="right" src="https://raw.github.com/cliffano/repomaestro/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/repomaestro/workflows/CI/badge.svg)](https://github.com/cliffano/repomaestro/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/repomaestro/badge.svg)](https://snyk.io/test/github/cliffano/repomaestro)
[![Dependencies Status](https://img.shields.io/librariesio/release/pypi/repomaestro)](https://libraries.io/github/cliffano/repomaestro)
[![Published Version](https://img.shields.io/pypi/v/repomaestro.svg)](https://pypi.python.org/pypi/repomaestro)
<br/>

Repo Maestro
------------

Repo Maestro is a code repositories configuration file manager.

It fetches repositories data from GitHub, stored in a Repo Maestro configuration file, and then generates output files using Jinja2 templates rendered with the repositories data.

Installation
------------

    pip3 install repomaestro

Usage
-----

Initialise a Repo Maestro configuration file with GitHub repositories data:

    GITHUB_TOKEN=<github_token> repomaestro init --conf-file .repomaestro.yaml --github-id cliffano

Please note that the fetched GitHub repositories data are based on the ones accessible using the provided `GITHUB_TOKEN`, which can include repositories owned by multiple users and orgs.

When `--github-ids` flag is provided, only the repositories owned by the specified user or org will be included in Repo Maestro configuration file.

Generate output file based on a Jinja2 template:

    repomaestro gen --conf-file path/to/.repomaestro.yaml --template-file path/to/some-template.j2 --out-file path/to/some-output.json

Show help guide:

    repomaestro --help

### Templates

Template parameters:

| Parameter | Description |
|-----------|-------------|
| `repos` | Repositories data with repository name as key and a map of repository properties `git_url`, `homepage`, `keywords`, and `ssh_url` as values. |

The `repos` parameter can then be used in Jinja2 templates like this:

```jinja2
{
  "repos": {
    {% for repo_name, repo_data in repos.items() %}
    "{{ repo_name }}": {
      "git_url": "{{ repo_data.git_url }}",
      "homepage": "{{ repo_data.homepage }}",
      "keywords": {{ repo_data.keywords }}
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  }
}
```

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
