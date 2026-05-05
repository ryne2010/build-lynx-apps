---
name: lynx-official-tools
description: Route Lynx.js framework, debugging, preview, trace, TypeScript, integration, desktop, SVG, routing, testing, bundle, Habitat, state-management, reactlynx-use, and tooling questions through official Lynx Docs MCP, Lynx DevTool MCP, llms.txt, AGENTS guidance, and community skills. Use for Lynx architecture, ReactLynx APIs, build/debug behavior, device preview, trace/debug workflows, ecosystem packages, or when current Lynx documentation is needed.
---

# Lynx Official Tools

Use this skill whenever a task depends on current Lynx.js framework behavior, ReactLynx APIs, debugging, preview, trace analysis, host integration, TypeScript, routing, testing, bundle behavior, Habitat dependency sync, state-management examples, `reactlynx-use`, or agent setup guidance.

## Source-of-truth order

1. **Configured Lynx Docs MCP first.** If the `lynx-docs` MCP is available, list its resources and read `lynx-docs://llms.txt` before reading task-specific resources.
2. **Official Lynx docs next.** If MCP resources are unavailable, use official Lynx docs and `https://lynxjs.org/llms.txt` as the fallback documentation surface.
3. **Community skills and bundled companions for domain rules.** Use the bundled companion skills in this plugin and, when installed, the upstream `lynx-community/skills` rule sets such as `reactlynx-best-practices`, `lynx-typescript`, `lynx-devtool`, `lynx-trace-record`, `lynx-trace-analysis`, `debug-info-remapping`, and `habitat-usage`.
4. **Local summaries are routing hints only.** Do not treat this skill as a fork of the Lynx documentation.

## Freshness and version gate

- For feature availability, release-specific behavior, or platform support, check `lynx-docs://versions.md` and the relevant release/blog resource such as `lynx-docs://blog/lynx-3-7.md` before making current-version claims.
- Distinguish `next` docs from latest stable docs. If only `next` evidence was checked, say so.
- Do not hardcode package versions from memory. Read the consuming app's `package.json`, lockfile, and Rspeedy config before recommending version-sensitive changes.
- For bundle/host compatibility claims, record `engineVersion` or the equivalent configured engine target when present.

## Setup references only

Do not run setup commands, install MCP servers, add community skills, or mutate configuration from this skill. For documentation and separate setup handoff only, mention:

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

## Required routing pattern

For any Lynx implementation question:

1. Identify whether the question is project/bundle creation, host integration, framework/API, ReactLynx code, UI composition, preview/debug, trace/performance, routing/testing, state management, ecosystem hooks, Habitat dependency sync, desktop/SVG, bundle reuse, or service integration.
2. For framework/API behavior, retrieve current official docs before coding or making claims.
3. For ReactLynx component code, route to `reactlynx-best-practices`; for TypeScript, DevTool, trace, or source-map diagnostics, route to the matching bundled companion skill after reading the relevant official resource.
4. For preview/debug, prefer Lynx DevTool MCP when configured and when a device/app is connected.
5. For UI composition with local components, route to `lynx-ui-guidance` after official framework constraints are understood.
6. For payments or data-layer work, route to the optional Stripe or Supabase/Postgres skills only after UI and framework boundaries are clear.

## Resource router matrix

| Request class | Official resources / skills to prefer | Evidence to record |
|---|---|---|
| Docs entrypoint | `lynx-docs://llms.txt`, `lynx-docs://ai/index.md`, `lynx-docs://ai/lynx-docs-mcp.md` | MCP available, `llms.txt` read, fallback used if any |
| Version/platform freshness | `lynx-docs://versions.md`, `lynx-docs://blog/lynx-3-7.md`, relevant platform docs | Latest/next docs checked, platform support caveat, package/version read from project |
| Lynx project/bundle quick start | `lynx-docs://react/start/quick-start.md`, `lynx-docs://rspeedy/start/quick-start.md`, `lynx-docs://rspeedy/output.md` | Project vs bundle claim, package manager commands as documentation only |
| Existing host integration | `lynx-docs://react/start/integrate-with-existing-apps.md`, `lynx-docs://guide/start/integrate-with-existing-apps.md` | Host platform, integration boundary, no full-host-app overclaim |
| ReactLynx dual-thread code | `lynx-docs://ai/skills/reactlynx-best-practices.md`, `lynx-docs://react/best-practices.md`, `lynx-docs://react/thinking-in-reactlynx.md`, local `reactlynx-best-practices` | Thread context, events, native APIs, main-thread script decision |
| Main-thread scripts / shared modules | `lynx-docs://react/main-thread-script.md`, `lynx-docs://guide/scripting-runtime/main-thread-runtime.md` | `main-thread:` use, `runOnMainThread`, `runOnBackground`, JSON-serializable captures, shared module limitations |
| TypeScript | `lynx-docs://ai/skills/lynx-typescript.md`, `lynx-docs://rspeedy/typescript.md`, local `lynx-typescript` | Env declarations, type extensions, `isolatedModules`, typecheck availability |
| Elements/layout/styling | `lynx-docs://guide/ui/elements-components.md`, `lynx-docs://api/elements/built-in/view.md`, `lynx-docs://api/elements/built-in/text.md`, `lynx-docs://api/elements/built-in/image.md`, `lynx-docs://api/elements/built-in/scroll-view.md`, `lynx-docs://api/elements/built-in/list.md`, `lynx-docs://guide/ui/styling.md`, `lynx-docs://guide/ui/layout/index.md` | Elements used, styling/layout caveats, CSS Modules/global token boundary |
| SVG/icons/charts | `lynx-docs://blog/lynx-3-7.md`, `lynx-docs://api/elements/built-in/svg.md` when available | SVG element availability, host compatibility, inline content vs `src`, fallback when docs resource unavailable |
| Event handling / direct manipulation | `lynx-docs://guide/interaction/event-handling.md`, `lynx-docs://guide/interaction/event-handling/event-propagation.md`, `lynx-docs://guide/interaction/event-handling/manipulating-element.react.md` | Event names, propagation, main/background thread choice |
| Desktop interactions | `lynx-docs://blog/lynx-3-7.md`, desktop API resources when listed | macOS/Windows support caveat, mouse/keyboard/wheel/cursor support, target host proof |
| Native modules / host data | `lynx-docs://guide/use-native-modules.md`, `lynx-docs://guide/use-data-from-host-platform.md` | Host API availability, background-thread safety, no invented modules |
| Networking/storage/data fetching | `lynx-docs://guide/interaction/networking.md`, `lynx-docs://guide/interaction/storage.md`, `lynx-docs://react/data-fetching.md` | Host service boundary, secret handling, Fetch differences, offline/fallback assumptions |
| Routing | `lynx-docs://react/routing/tanstack-router.md`, `lynx-docs://react/routing/react-router.md` | Memory routing/browser history caveat, `document`/`isServer` handling, polyfills, generated routes |
| Testing | `lynx-docs://react/reactlynx-testing-library.md` | Rstest/Vitest setup, `render`/`fireEvent`, list/main-thread test caveats, available project scripts |
| React Compiler / render optimization | `lynx-docs://react/react-compiler.md`, `lynx-docs://react/best-practices.md` | Compiler enabled or not, hoisting/memo decision, no unsupported optimization claim |
| Code splitting / lazy bundles | `lynx-docs://react/code-splitting.md`, `lynx-docs://rspeedy/output.md` | Bundle boundary, CSS scope caveat, lazy bundle setup, runtime loading path |
| External bundles / shared component bundles | `lynx-docs://rspeedy/external-bundle.md` | Producer/consumer split, section names, `externalsPresets`, CSS/engineVersion requirement |
| State management | `lynx-docs://react/state-management/jotai.md`, `lynx-docs://react/state-management/valtio.md`, `lynx-docs://react/state-management/zustand.md` | Store library already present or proposed, background/main-thread boundary, no new dependency unless scoped |
| Ecosystem hooks / reactlynx-use | `lynx-docs://blog/lynx-3-6.md`, current `reactlynx-use` docs when available, project `package.json` | `reactlynx-use` dependency present/absent, hook utility reason, fallback to official ReactLynx APIs |
| Habitat / multi-repo sync | upstream `lynx-community/skills` `habitat-usage`, `.habitat`, `DEPS`, project wrapper/docs | Habitat version/wrapper, sync command/log, auth/network/integrity caveat, no destructive overwrite |
| DevTool preview/debug | `lynx-docs://ai/lynx-devtool-mcp.md`, `lynx-docs://guide/devtool.md`, `lynx-docs://ai/skills/lynx-devtool.md`, local `lynx-devtool` | DevTool MCP available, device/app connected, CDP commands/App commands/Open URLs/Troubleshooting/inspection evidence, tools used |
| Trace/performance | `lynx-docs://guide/devtool/trace.md`, `lynx-docs://ai/skills/trace-record.md`, `lynx-docs://ai/skills/trace-analysis.md`, `lynx-docs://react/performance/profiling.md`, `lynx-docs://guide/performance/metrics/performance-api.md`, local `lynx-trace-record`, local `lynx-trace-analysis` | Trace artifact or fallback, profiling scope, no fabricated metrics |
| Debug-info/source mapping | `lynx-docs://ai/skills/debug-info-remapping.md`, `lynx-docs://rspeedy/output.md`, local `debug-info-remapping` | Source-stack mapping method, loaded source reference |
| Accessibility/i18n | `lynx-docs://guide/inclusion/accessibility.md`, `lynx-docs://guide/inclusion/internationalization.md` | Target host accessibility/i18n caveats |

## Lynx DevTool MCP usage

When available and connected to a device/app, Lynx DevTool MCP can support:

- read-only element/style inspection,
- CDP commands for supported read-only DOM/CSS/console/source/screenshot operations,
- App commands for opening or closing pages in a connected Lynx application,
- Open URLs for launching a route/card URL in the connected app,
- troubleshooting connector, transport, device discovery, and app visibility issues,
- console and stack-trace review,
- source lookup for loaded JavaScript,
- tap/drag-style interactions,
- screenshots for multimodal review,
- trace/debug workflows when supported by the installed DevTool surface.

DevTool MCP inspection is read-only. Modify source files to change the app.

## Official-tool ledger

Include a compact ledger for any Lynx-framework answer:

- Docs MCP available: yes/no/unknown.
- `lynx-docs://llms.txt` read: yes/no/fallback reason.
- Task-specific resources read: list resource URIs or official docs URLs.
- Latest/version resource checked when relevant: yes/no/not needed.
- Community/bundled companion skill used or checked: list if available.
- DevTool MCP available: yes/no/unknown.
- Device/app connected: yes/no/not needed.
- Target host/platform: list or not specified.
- Evidence tier: screenshot/runtime, static/build, or planning-only.
- Fallback source and confidence if MCP/DevTool was unavailable.

## Evidence rules

- Cite which official Lynx page or MCP resource was used for framework claims.
- Record whether DevTool MCP/device preview was available.
- Do not claim screenshot, trace, runtime, desktop, SVG, routing, bundle, testing, or visual parity evidence unless the relevant artifact or docs were actually checked.
- Do not run setup/configuration commands from this skill.
