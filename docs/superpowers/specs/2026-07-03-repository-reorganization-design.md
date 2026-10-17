# Repository Reorganization Design

## Goal

Rename the project from `ml-algos-from-scratch` to `algos-from-scratch` and
organize its implementations under the two top-level domains `dsa/` and `ml/`.

## Target structure

```text
algos-from-scratch/
├── dsa/
│   └── palindrome.py
├── ml/
│   ├── in_numpy/
│   ├── in_torch/
│   └── sandbox/
│       └── classifier_with_imbalance_class.py
├── README.md
└── pyproject.toml
```

`dsa/` remains at the repository root. The existing `in_numpy/` and
`in_torch/` trees move unchanged under `ml/`. The sandbox belongs under `ml/`
because the exercise uses scikit-learn and imbalanced-learn rather than a
general data-structures-and-algorithms technique.

## Rename scope

The rename covers all visible repository identities:

- local directory: `ml_algos-from-scratch` to `algos-from-scratch`;
- GitHub repository: `komaksym/ml_algos-from-scratch` to
  `komaksym/algos-from-scratch`;
- Git remote URL (SSH or HTTPS);
- Python project name in `pyproject.toml`;
- README title and description.

The GitHub rename must happen before updating the local remote. Renaming the
local directory happens last because it changes the working path used by tools
and the IDE.

## Screenshot exercise

Create `ml/sandbox/classifier_with_imbalance_class.py` as an intentionally
incomplete starter matching the screenshot's public shape:

- import `make_pipeline` from `imblearn.pipeline`;
- import `LinearSVC` from `sklearn.svm`;
- define `ClassifierWithImbalanceClass`;
- initialize a pipeline containing `LinearSVC`;
- leave `train` and `predict` for the user to implement.

Add scikit-learn and imbalanced-learn to the development dependency group
because the sandbox is a development exercise rather than part of the
package's runtime surface.

The same classifier file will generate a deterministic imbalanced
binary-classification dataset, split it with stratification, train the wrapper,
calculate ROC AUC from its predictions, and print the score when run directly.

## Existing work and scope control

Preserve all current user changes, including the deletions of
`in_numpy/main.py` and `in_numpy/sandbox.py`. Do not refactor implementations
while moving them. Git should represent the directory reorganization as
renames where content is unchanged.

## Documentation

Update the README description and layout to cover both DSA and ML work. Explain
that `ml/sandbox/` contains incomplete exercises. Update the package name and
description in `pyproject.toml` without changing the version or dependencies.

## Validation

After the moves and metadata edits:

1. run Ruff formatting and lint checks across the repository;
2. compile all tracked Python files to catch syntax errors without importing
   them;
3. run the classifier file and confirm it prints a valid ROC AUC score;
4. run the existing palindrome checks;
5. build the Python project with `uv build`;
6. inspect `git diff --check`, the resulting tree, project metadata, remote URL,
   GitHub repository name, and final local directory name.
