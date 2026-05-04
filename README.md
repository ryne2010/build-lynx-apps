# Build Lynx Apps Plugin

Builder workflows for Lynx.js apps, official Lynx AI tooling, Lynx-native UI composition with `@dumbooks/lynx-ui`, and optional app-service integrations.

## Skills

- `lynx-app-builder` — concept-first Lynx app workflow with implementation and evidence-based visual verification.
- `lynx-official-tools` — routes Lynx framework, debugging, and tooling questions to official Lynx Docs MCP, DevTool MCP, `llms.txt`, AGENTS guidance, and community skills.
- `lynx-ui-guidance` — read-only `@dumbooks/lynx-ui` usage guidance, package-import-first component selection, proof gates, and guarded CLI boundaries.
- `stripe-best-practices` — optional service-domain guidance for payment flows used by Lynx apps.
- `supabase-best-practices` — optional service-domain guidance for Postgres/Supabase data layers used by Lynx apps.

## Purpose

Use this plugin when building or reviewing Lynx.js app surfaces. It preserves a high-taste concept → implementation → verification workflow while routing Lynx framework truth to official Lynx sources and replacing DOM-oriented component assumptions with Lynx-native `lynx-ui` guidance.

## Official Lynx tooling setup references

These commands are documentation only. Do not run setup or mutate user configuration unless the user explicitly requests setup mode.

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

When `lynx-docs` MCP is configured, agents should list resources and read `lynx-docs://llms.txt` first, then read the specific docs needed for the task. When `lynx-devtool` MCP is configured and a device/app is connected, agents may use it for inspection, console/source diagnostics, interaction, and screenshots; source code remains the mutation surface.
