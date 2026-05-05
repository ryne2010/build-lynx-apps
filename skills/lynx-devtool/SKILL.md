---
name: lynx-devtool
description: First-class Lynx DevTool MCP workflow guidance for connected-device/app inspection, CDP commands, App commands, Open URLs, troubleshooting, console/source debugging, interaction, screenshots, visual QA, and runtime verification. Use when debugging, previewing, opening pages/URLs, taking screenshots, checking console/source state, interacting with a Lynx page, diagnosing connector issues, or proving visual/runtime behavior.
---

# Lynx DevTool

Use this skill when a Lynx task needs runtime evidence from a connected Lynx app/device: CDP-backed element/style inspection, App commands, Open URLs, connector/transport troubleshooting, console logs, loaded source lookup, tap/drag interactions, screenshots, trace capture handoff, or visual QA evidence.

This skill is a wrapper over official Lynx DevTool docs/MCP behavior. It does not install or configure DevTool by itself.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/lynx-devtool-mcp.md` — Lynx DevTool MCP setup and tool categories.
- `lynx-docs://ai/skills/lynx-devtool.md` — official skill overview.
- `lynx-docs://guide/devtool.md` — Lynx DevTool behavior.
- `lynx-docs://guide/devtool/trace.md` — trace workflow when performance capture is involved.
- `lynx-docs://ai/skills/debug-info-remapping.md` — source remapping handoff for minified/main-thread errors.

## Hard boundaries

- Do not run setup commands, add MCP servers, or mutate user configuration unless the user starts a separate setup task.
- DevTool MCP inspection is read-only. Modify source files, not the runtime element tree, to make durable changes.
- Do not claim DevTool, screenshot, source, interaction, or console evidence unless the relevant MCP/device/app artifact was actually inspected.
- If no device/app is connected, fall back to static/build/type/lint/test evidence and state that runtime evidence is unavailable.
- Do not use web Browser/IAB evidence as a substitute for Lynx runtime evidence unless the target is explicitly Lynx for Web and the limitation is stated.
- Treat App commands and Open URLs as connected-app preview/navigation operations, not as permission to change MCP setup, install apps, or mutate project configuration.
- Preserve connector/transport troubleshooting output exactly enough for follow-up diagnosis, but redact secrets, device tokens, private URLs, and credentials.

## Workflow

1. Record availability:
   - Docs MCP available and `lynx-docs://llms.txt` read.
   - DevTool MCP configured: yes/no/unknown.
   - Connected device/app/page (connected device/app): device type, app/page identifier, route/card URL, and host platform.
2. Choose the official DevTool operation class before acting:
   - **CDP commands:** read-only DOM/CSS-style queries, console retrieval, source lookup, and screenshots where the installed MCP exposes CDP-like tools.
   - **App commands:** open or close pages in the connected Lynx application when navigation/page lifecycle is the debugging target.
   - **Open URLs:** launch a route/card URL directly in Lynx for development/testing when the host supports it.
   - **Troubleshooting:** diagnose connector, transport, device discovery, app visibility, or MCP capability issues before falling back.
3. Inspect runtime evidence as needed:
   - element/style tree for layout and state,
   - console messages and stack traces,
   - loaded sources for source/error correlation,
   - user interactions such as tap or drag,
   - screenshots for visual review,
   - App command/Open URL result when page navigation is under test,
   - troubleshooting diagnostics when connection or transport fails.
4. For visual work, hand screenshot/reference comparison to `$visual-verdict` only when both an approved reference and generated/current screenshot exist.
5. For performance capture, hand off to `lynx-trace-record` and then `lynx-trace-analysis`.
6. For minified source or main-thread runtime errors, hand off to `debug-info-remapping`.
7. Report evidence tier clearly: Lynx runtime/screenshot, static/build fallback, or planning-only.

## Output ledger

Include:

- DevTool MCP configured: yes/no/unknown,
- device/app connected: yes/no/not needed,
- route/card URL and host platform,
- DevTool operation class used: CDP commands/App commands/Open URLs/Troubleshooting/inspection/console/source/interaction/screenshot,
- tools or evidence inspected,
- screenshot/trace/source artifact paths when applicable,
- console/source findings,
- interaction path checked,
- App command/Open URL or troubleshooting output summary when applicable,
- fallback reason if runtime evidence was unavailable.
