#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "$0")/.."

ruff format --check .
ruff check .
python3 -m compileall -q dsa ml tests
python3 -m unittest discover -s tests -v
uv build
