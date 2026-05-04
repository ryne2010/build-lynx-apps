---
name: lynx-official-tools
description: Route Lynx.js framework, debugging, preview, and tooling questions through official Lynx Docs MCP, Lynx DevTool MCP, llms.txt, AGENTS guidance, and community skills. Use for Lynx architecture, ReactLynx APIs, build/debug behavior, device preview, trace/debug workflows, or when current Lynx documentation is needed.
---

# Lynx Official Tools

Use this skill whenever a task depends on current Lynx.js framework behavior, ReactLynx APIs, debugging, preview, trace analysis, or agent setup guidance.

## Source-of-truth order

1. **Configured Lynx Docs MCP first.** If the `lynx-docs` MCP is available, list its resources and read `lynx-docs://llms.txt` before reading task-specific resources.
2. **Official Lynx docs next.** If MCP resources are unavailable, use official Lynx docs and `https://lynxjs.org/llms.txt` as the fallback documentation surface.
3. **Community skills for domain rules.** When installed, use `lynx-community/skills` for reusable Lynx rule sets such as ReactLynx best practices, TypeScript, DevTool, trace recording, trace analysis, and debug-info remapping.
4. **Local summaries are routing hints only.** Do not treat this skill as a fork of the Lynx documentation.

## Setup references only

Do not run setup commands unless the user explicitly requests setup/configuration mode. For documentation and handoff, use:

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

## Required routing pattern

For any Lynx implementation question:

1. Identify whether the question is framework/API, UI composition, preview/debug, or service integration.
2. For framework/API behavior, retrieve current official docs before coding or making claims.
3. For preview/debug, prefer Lynx DevTool MCP when configured and when a device/app is connected.
4. For UI composition with local components, route to `lynx-ui-guidance` after official framework constraints are understood.
5. For payments or data-layer work, route to the optional Stripe or Supabase/Postgres skills only after UI and framework boundaries are clear.

## Lynx DevTool MCP usage

When available, Lynx DevTool MCP can support:

- element/style inspection through read-only tooling,
- console and stack-trace review,
- source lookup for loaded JavaScript,
- tap/drag-style interactions,
- screenshots for multimodal review.

DevTool MCP inspection is read-only. Modify source files to change the app.

## Evidence rules

- Cite which official Lynx page or MCP resource was used for framework claims.
- Record whether DevTool MCP/device preview was available.
- Do not claim screenshot or visual parity unless a screenshot artifact was actually captured and compared.
