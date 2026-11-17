<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 33765f324ad3f2316a50f31a053a2dd03f9ca9f03c39fd7a3b06e919af9668c8 -->

# gdam-test-addon

Minimal Godot addon fixture. Its manifest and entrypoint are validated together; runtime integration is exercised by consuming projects.

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. Use `mise tasks ls` to inspect the applicable stages.

For contributor verification, prepare the pinned helper source before running native tasks:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach 71540eb673ebd47162de3b78bb6ffbf77605d2ab
mise install
mise run check
```

Declared tests produce source evidence from the current verification session in `.artifacts/verification`.

## Contributor task interface

Contributor tool versions and task entry points live in the native Mise configuration. Use `mise run lint` for source checks, `mise run test` for the applicable behavioral tests, and `mise run check` for the complete supported gate. `mise run clean` removes declared generated outputs while preserving source, credentials and retained data. This package has no application development service.
