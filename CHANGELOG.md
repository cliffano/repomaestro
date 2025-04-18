# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.0.0 - 2025-04-18
### Changed
- Change minimum Python to 3.11

### Fixed
- Fix ssh_url due to empty value from PyGithub.Repository

## 1.1.0 - 2025-04-13
### Added
- Add ssh_url to repository properties map

## 1.0.0 - 2025-01-06
### Added
- Add --exclude-keywords flag to gen-file command

### Changed
- Rename flag --filter-keywords to --include-keywords
- Upgrade PieMaker to 1.8.0

### Removed
- Remove redundant log messages

## 0.10.1 - 2024-12-25
### Fixed
- Fix publish token parameter passing

## 0.10.0 - 2024-12-25
### Added
- Initial version
