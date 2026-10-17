# Plans

## Repo Tooling Setup

Summary: configure this repository as a small Python/uv workspace for ML algorithm interview practice, with `prek` and `pre-commit` sharing one hook config.

Milestones:

1. Configure project metadata, runtime dependencies, dev dependencies, Ruff, and file ignore rules.
2. Add compatible `prek`/`pre-commit` hooks for Ruff formatting/linting and basic file hygiene.
3. Remove notebook checkpoint files from the Git index while preserving local copies.
4. Sync dependencies, install the `prek` Git hook shim, and run validation through both hook runners.

## Repository Reorganization

Summary: rename the project to `algos-from-scratch`, separate DSA and ML code,
and add an intentionally incomplete ML sandbox with a deterministic ROC AUC
benchmark.

Milestones:

1. Move NumPy and PyTorch implementations under `ml/` without changing their contents.
2. Add the imbalanced-classification starter and ROC AUC harness in one file.
3. Update project metadata, dependencies, lockfile, and repository documentation.
4. Run lint, compilation, tests, the palindrome checks, and the package build.
5. Rename the GitHub repository, remote URL, and local working directory.

## Source recovery

Summary. Preserve the pending reorganization and the user classifier experiment in one review branch. Keep local datasets out of the public repository.

- [x] Capture the exact source and review publication paths.
- [x] Replay layout and metadata checks against main before restoring the source.
- [ ] Restore the recorded source without changing algorithm behavior.
- [ ] Verify formatting, syntax, palindrome examples and packaging.
- [ ] Review, commit and sync the complete source packet.

Earlier exercise checkboxes describe prior work. They do not verify the current classifier, which reads local Downloads data and remains outside this recovery gate.
