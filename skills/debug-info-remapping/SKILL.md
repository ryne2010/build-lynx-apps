---
name: debug-info-remapping
description: First-class Lynx debug-info remapping guidance for minified, bundled, or main-thread runtime errors. Use when console stacks, bytecode positions, source maps, generated sources, or loaded DevTool sources must be mapped back to original ReactLynx source.
license: MIT
---

# Debug Info Remapping

Use this skill when a Lynx console/runtime/main-thread error points at generated, minified, bytecode, or bundle positions and the original source location is unclear.

This is a diagnostic skill. Remap evidence first; do not guess the source file or patch code before the mapping is grounded.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/skills/debug-info-remapping.md` — official skill overview.
- `lynx-docs://ai/lynx-devtool-mcp.md` — DevTool source/console access.
- `lynx-docs://guide/devtool.md` — DevTool behavior.
- `lynx-docs://rspeedy/output.md` — output and source map artifacts.
- `lynx-docs://react/main-thread-script.md` — main-thread script error context.

## Remapping workflow

1. Capture the exact error message, stack, generated file, line/column or bytecode position, runtime thread, and host/platform.
2. Use `lynx-devtool` when connected to read console entries and loaded JavaScript sources.
3. Locate build artifacts and source maps from the consuming app's output configuration (`dist`, `.rspeedy`, `output.sourceMap`, `DEBUG=rspeedy` artifacts when available).
4. Map generated positions back to original file/function/line. If only approximate mapping is possible, state that explicitly.
5. Classify thread context: main thread script, background thread, render/JSX evaluation, effect/event handler, native module, or host service callback.
6. Hand off to the right implementation skill only after mapping is grounded.

## Evidence rules

- Do not claim a source location without mapping evidence from DevTool sources, source maps, generated output, or direct repository correspondence.
- Do not conflate main-thread generated code with background-thread source.
- Do not disable minification/source maps as the primary fix unless the task is specifically about debug build configuration.
- Do not expose secrets from logs, source maps, environment, or private build artifacts.

## Output ledger

Include:

- error/stack excerpt location,
- generated artifact and source map inspected,
- original source mapping result,
- confidence level,
- thread/runtime classification,
- next diagnostic or fix target.
