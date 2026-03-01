#!/usr/bin/env python3
"""Premium runtime checker (safe, 2026-ready).

This utility replaces legacy unsupported automation with a secure diagnostics
workflow that helps users verify their local environment.
"""

from __future__ import annotations

import argparse
import importlib
import json
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

MIN_PYTHON = (3, 10)
RECOMMENDED_PYTHON = (3, 12)
REQUIRED_MODULES = ("requests", "rich", "bs4")


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


def _check_python() -> CheckResult:
    version = sys.version_info[:3]
    ok = version >= MIN_PYTHON
    status = f"Python {version[0]}.{version[1]}.{version[2]}"
    if version < RECOMMENDED_PYTHON:
        status += f" (recommended {RECOMMENDED_PYTHON[0]}.{RECOMMENDED_PYTHON[1]}+)"
    return CheckResult("python", ok, status)


def _check_command(cmd: str) -> CheckResult:
    path = shutil.which(cmd)
    return CheckResult(cmd, path is not None, path or "not found in PATH")


def _check_modules() -> list[CheckResult]:
    results: list[CheckResult] = []
    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
            results.append(CheckResult(f"module:{module}", True, "installed"))
        except ModuleNotFoundError:
            results.append(CheckResult(f"module:{module}", False, "missing"))
    return results


def _check_git_repo() -> CheckResult:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--is-inside-work-tree"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return CheckResult("git_repo", out == "true", out)
    except Exception:
        return CheckResult("git_repo", False, "unable to validate repository")


def run_checks() -> list[CheckResult]:
    results = [
        _check_python(),
        _check_command("git"),
        _check_command("pip"),
        _check_git_repo(),
    ]
    results.extend(_check_modules())
    return results


def print_human(results: list[CheckResult]) -> int:
    print("Premium Environment Check (2026)")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print(f"Platform : {platform.platform()}")
    print("-" * 48)

    has_error = False
    for result in results:
        mark = "OK" if result.ok else "FAIL"
        print(f"[{mark:4}] {result.name:16} {result.detail}")
        if not result.ok:
            has_error = True

    print("-" * 48)
    if has_error:
        print("Some checks failed. Install missing dependencies and retry.")
        return 1

    print("All checks passed. Your environment is ready.")
    return 0


def print_json(results: list[CheckResult]) -> int:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results": [asdict(item) for item in results],
        "ok": all(item.ok for item in results),
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["ok"] else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether this environment is ready for the Premium utilities.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON instead of plain text.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run_checks()
    if args.json:
        return print_json(results)
    return print_human(results)


if __name__ == "__main__":
    raise SystemExit(main())
