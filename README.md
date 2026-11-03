<!-- Generated from private documentation source. Do not edit directly. Source SHA256: a923618f706165103cf22adec4ca382b7bff52b338c8d6df9c963b93d3e4402c -->

# gdam-test-addon

Minimal Godot addon fixture. Its manifest and entrypoint are validated together; runtime integration is exercised by consuming projects.

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. Use `mise tasks ls` to inspect the applicable stages.

For contributor verification, prepare the pinned helper source before running native tasks:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach f7e243524ce2aa29f299e4c79db33001f72f4a30
mise install
mise run check
```

Declared tests produce source evidence from the current verification session in `.artifacts/verification`.

## Contributor task interface

Contributor tool versions and task entry points live in the native Mise configuration. Use `mise run lint` for source checks, `mise run test` for the applicable behavioral tests, and `mise run check` for the complete supported gate. `mise run clean` removes declared generated outputs while preserving source, credentials and retained data. This package has no application development service.
