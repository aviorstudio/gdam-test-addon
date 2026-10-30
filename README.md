<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 11127f17367c1758bc6ab7cd6ce305353bd8552f255f284837f8e79a049139c5 -->

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
