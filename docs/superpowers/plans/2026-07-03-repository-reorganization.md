# Repository Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename and reorganize the repository around DSA and ML domains, with a runnable ROC AUC exercise sandbox.

**Architecture:** Keep DSA at the root and move existing ML implementations unchanged under `ml/`. Keep the screenshot exercise and its executable ROC AUC harness in one sandbox file.

**Tech Stack:** Python 3.13, uv, NumPy, PyTorch, scikit-learn, imbalanced-learn, Ruff

---

### Task 1: Reorganize ML implementations

**Files:**
- Move: `in_numpy/*.py` to `ml/in_numpy/*.py`
- Move: `in_torch/*.py` to `ml/in_torch/*.py`

- [x] Create `ml/` and move both implementation directories beneath it.
- [x] Confirm Git detects unchanged files as renames and preserves the user's existing deletions of `in_numpy/main.py` and `in_numpy/sandbox.py`.

### Task 2: Add the classification sandbox

**Files:**
- Create: `ml/sandbox/classifier_with_imbalance_class.py`

- [x] Create the screenshot's class skeleton with `LinearSVC` inside an imbalanced-learn pipeline.
- [x] Add a deterministic, stratified imbalanced dataset harness in the same file.
- [x] Run `uv run python ml/sandbox/classifier_with_imbalance_class.py` and expect a printed ROC AUC score.

### Task 3: Update project identity and documentation

**Files:**
- Modify: `pyproject.toml`
- Modify: `uv.lock`
- Modify: `README.md`

- [x] Change the project name and description to cover general algorithms.
- [x] Add scikit-learn and imbalanced-learn to the development dependency group and refresh `uv.lock`.
- [x] Document the `dsa/`, `ml/in_numpy/`, `ml/in_torch/`, and `ml/sandbox/` layout and the ROC AUC command.

### Task 4: Validate local changes

**Files:**
- Validate: all tracked project files

- [x] Run `uv run ruff format --check .` and `uv run ruff check .`.
- [x] Compile tracked Python files with `python3 -m compileall -q dsa ml`.
- [x] Run the sandbox file and confirm it prints a valid ROC AUC score.
- [x] Run `python3 dsa/palindrome.py` and confirm every case passes.
- [x] Run `uv build` and `git diff --check`.

### Task 5: Rename repository surfaces

**Files:**
- External: GitHub repository `komaksym/ml_algos-from-scratch`
- Modify: Git remote `origin`
- Move: `/Users/koval/dev/ml_algos-from-scratch` to `/Users/koval/dev/algos-from-scratch`

- [x] Authenticate GitHub CLI if required, then rename the GitHub repository to `algos-from-scratch`.
- [x] Verify `origin` points to `komaksym/algos-from-scratch`.
- [x] Rename the local directory last and verify the final path and Git status from its new location.
