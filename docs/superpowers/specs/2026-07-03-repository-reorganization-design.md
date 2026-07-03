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
│       └── classifier_with_imbalanced_class.py
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
- Git remote URL;
- Python project name in `pyproject.toml`;
- README title and description.

The GitHub rename must happen before updating the local remote. Renaming the
local directory happens last because it changes the working path used by tools
and the IDE.

## Screenshot exercise

Create `ml/sandbox/classifier_with_imbalanced_class.py` as an intentionally
incomplete starter matching the screenshot's public shape:

- import `make_pipeline` from `imblearn.pipeline`;
- import `LinearSVC` from `sklearn.svm`;
- define `ClassifierWithImbalancedClass`;
- initialize a pipeline containing `LinearSVC`;
- leave `train` and `predict` for the user to implement.

Do not add scikit-learn or imbalanced-learn to project dependencies yet. The
file is an exercise prompt, not part of the runnable project surface. Its
docstring will state the optional packages required when the user is ready to
run it.

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
   optional exercise dependencies;
3. run the existing palindrome checks;
4. build the Python project with `uv build`;
5. inspect `git diff --check`, the resulting tree, project metadata, remote URL,
   GitHub repository name, and final local directory name.

The incomplete sandbox is validated syntactically only because importing it
requires dependencies intentionally excluded from the project.
