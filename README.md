# Algorithms From Scratch

Small Python workspace for data-structure, algorithm, and machine-learning
interview exercises. It includes from-scratch NumPy implementations, PyTorch
training components, and isolated practice sandboxes.

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

## Layout

- `dsa/`: data-structure and algorithm exercises.
- `ml/in_numpy/`: NumPy-first machine-learning implementations.
- `ml/in_torch/`: PyTorch implementations and training components.
- `ml/sandbox/`: intentionally incomplete ML exercises and their tests.

## Imbalanced classification exercise

Implement `train()` and `predict()` in
`ml/sandbox/classifier_with_imbalance_class.py`, then run that same file:

```bash
uv run python ml/sandbox/classifier_with_imbalance_class.py
```

The script trains the classifier and prints the solution's ROC AUC score.
