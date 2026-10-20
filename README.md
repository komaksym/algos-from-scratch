# ML Algorithms From Scratch

Small Python workspace for implementing classic ML and PyTorch interview exercises from scratch: training loops, simple neural nets, optimization basics, attention blocks, and similar junior ML engineer practice.

## Setup

```bash
uv sync --group dev
uv run prek install --overwrite --hook-type pre-commit
uv run prek install --overwrite --hook-type commit-msg
```

`prek` is the installed Git hook runner because it is fast. The same hook config also works with `pre-commit`.

## Checks

```bash
uv run prek run --all-files
uv run pre-commit run --all-files
```

Commit messages are checked with Commitizen, so use conventional commits like `feat: add feedforward block` or `fix: correct tensor shape`.

Direct Ruff checks:

```bash
uv run ruff format --check .
uv run ruff check .
```

The `stable-ci` job runs on every pull request and push to `main` with Python 3.13.
It uses Ruff 0.15.12 from `uv.lock`, compiles the sources, and runs the palindrome examples.
The job rejects a failed example even though the current example runner exits successfully on a mismatch.
It does not install NumPy or PyTorch, run training, or validate those implementations at runtime.

## Layout

- `in_numpy/`: NumPy-first implementations for fundamentals.
- `in_torch/`: PyTorch implementations and interview-style training loops.
