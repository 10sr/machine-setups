#!/usr/bin/env python3

import subprocess
import sys

import toml


def get_version_installed(module: str) -> str:
    out = subprocess.check_output(
        ["pipenv", "run", "python", "-m", "pip", "freeze"], encoding="utf-8"
    )
    for l in out.split("\n"):
        if l.startswith(module + "=="):
            return l.split("==")[1]
    raise Exception(f"Module {module} not found")


def get_version_required(module: str) -> str:
    with open("Pipfile") as f:
        obj = toml.load(f)
    return obj["packages"]["ansible"].lstrip("=")


def main():
    assert get_version_installed("ansible") == get_version_required("ansible")
    return 0


if __name__ == "__main__":
    sys.exit(main())
