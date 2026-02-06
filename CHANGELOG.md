# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Dependencies**: Added `ruamel-yaml = "^0.18.0"` to project dependencies in `pyproject.toml`

### Fixed
- **Critical syntax error in evaluator** (marble/evaluator/evaluator.py:324): Fixed incorrect indentation in `parse_research_ratings()` method
  - Corrected `except json.JSONDecodeError` block to align with `try` statement (was incorrectly nested inside `if` block)
  - Moved `else` clause to properly pair with `if` statement inside try block
  - This was a Python `SyntaxError` that prevented the module from being imported at all

- **Werewolf Unix/Linux compatibility** (f060bab): Fixed Windows-style paths (backslashes) to Unix-style paths (forward slashes) in werewolf scripts and config files
  - Updated `scripts/werewolf/run_simulation.sh` to use forward slashes and fixed corrupted command
  - Updated `scripts/werewolf/run_evaluation.sh` to use forward slashes
  - Updated `marble/configs/test_config/werewolf_config/werewolf_config.yaml` to use forward slashes in `system_prompt_path`
  - Removed corrupted arguments from run_simulation.sh, relying on argparse defaults for scientific integrity

- **Logger configuration** (bfe5503): Made file logging optional and configurable
  - Changed `log_to_file` parameter from unused boolean to `Optional[str]` for custom log file paths
  - Added automatic directory creation with `parents=True` for nested log paths
  - File logging now defaults to `None` (console only) for safer default behavior
  - Removed unused/commented-out file handler code

### Changed
- Updated `pyproject.toml` metadata

---

## Prior History

For commits before this fork, see the original [MARBLE repository](https://github.com/MultiagentBench/MARBLE).
