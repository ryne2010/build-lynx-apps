# Build Lynx Apps Plugin

Builder workflows for Lynx.js app surfaces, pages, projects, and bundles, official Lynx AI tooling, first-class official Lynx skill companions, ReactLynx best-practice guardrails, local-workspace UI composition with `@dumbooks/lynx-ui`, measured OMX visual QA loops, and optional app-service integration guidance.

## Skills

- `lynx-app-builder` — concept-first Lynx surface workflow with implementation inventories, OMX visual orchestration, and evidence-based verification.
- `lynx-official-tools` — routes Lynx framework, debugging, trace, TypeScript, integration, routing, testing, bundle, desktop, SVG, Habitat, state-management, `reactlynx-use`, and tooling questions to official Lynx Docs MCP, DevTool MCP, `llms.txt`, AGENTS guidance, and community skills.
- `reactlynx-best-practices` — first-class ReactLynx guardrails for dual-thread native API calls, events, main-thread scripts, cross-thread calls, shared modules, static JSX, TypeScript, testing, routing, data fetching, and bundle behavior.
- `lynx-typescript` — first-class TypeScript guardrails for Rspeedy env declarations, JSX config, CSS Modules, native modules, custom elements, InitData, GlobalProps, main-thread event/ref types, and package type boundaries.
- `lynx-devtool` — first-class DevTool MCP workflow guidance for connected-device inspection, CDP commands, App commands, Open URLs, troubleshooting, console/source debugging, interaction checks, screenshots, and runtime evidence ledgers.
- `lynx-trace-record` — first-class trace-capture guidance for startup, scroll, interaction, render, JS profiling, and native-module latency investigations.
- `lynx-trace-analysis` — first-class trace-analysis guidance for startup/white-screen metrics, smoothness, interaction latency, render pipeline, ReactLynx render churn, and native-module bottlenecks.
- `debug-info-remapping` — first-class debug-info remapping guidance for minified, bundled, source-map, or main-thread runtime errors.
- `lynx-ui-guidance` — read-only local-workspace `@dumbooks/lynx-ui` usage guidance, package-import-first component selection, proof gates, official-substrate metadata, local/internal-beta caveats, and guarded CLI boundaries.
- `stripe-best-practices` — optional service-domain guidance for payment flows used by Lynx app surfaces.
- `supabase-postgres-best-practices` — optional service-domain guidance for Postgres/Supabase data layers used by Lynx app surfaces.


## Install and distribution

This repository supports the current `gh skill` path for installing individual Agent Skills. It also includes Codex plugin marketplace metadata so the repository can be added as a Codex plugin marketplace source.

No release has been published by this repository setup step. As the sole maintainer, validate locally first, then publish a tagged release only when you are ready.

### Install individual skills with GitHub CLI

Install a specific skill for Codex at user scope:

```bash
gh skill install ryne2010/build-lynx-apps lynx-app-builder --agent codex --scope user
```

Preview skills before installing:

```bash
gh skill preview ryne2010/build-lynx-apps
gh skill preview ryne2010/build-lynx-apps reactlynx-best-practices
```

Search for published/discoverable skills from this owner:

```bash
gh skill search lynx --owner ryne2010
```

Install other bundled skills by name, for example:

```bash
gh skill install ryne2010/build-lynx-apps reactlynx-best-practices --agent codex --scope user
gh skill install ryne2010/build-lynx-apps lynx-official-tools --agent codex --scope user
gh skill install ryne2010/build-lynx-apps lynx-devtool --agent codex --scope user
gh skill install ryne2010/build-lynx-apps supabase-postgres-best-practices --agent codex --scope user
```

Update installed skills later:

```bash
gh skill update --all
```

### Maintainer validation and future publishing

Validate without uploading or creating a release:

```bash
python3 scripts/check_bundle.py
gh skill publish --dry-run .
```

When ready to publish, create a tagged GitHub release through `gh skill publish`:

```bash
gh skill publish --tag v0.1.0
```

Do not run the non-dry-run publish command until the intended tag, README, skill metadata, and repository contents are final. As the sole maintainer, also consider adding a GitHub tag-protection ruleset before the first public release so published versions remain immutable.

### Codex plugin marketplace setup

This repo includes `.agents/plugins/marketplace.json` plus `.codex-plugin/plugin.json`, so Codex can treat the repository as a plugin marketplace source. Add the marketplace from a local checkout or GitHub repository source:

```bash
codex plugin marketplace add ryne2010/build-lynx-apps
```

For local testing from this checkout, use the local path instead:

```bash
codex plugin marketplace add /path/to/build-lynx-apps
```

After adding the marketplace, install or enable the `build-lynx-apps` plugin from Codex's plugin UI when available in your Codex surface.

## Purpose

Use this plugin when building, reviewing, or planning Lynx.js app surfaces, pages, projects, and bundles. It preserves a high-taste concept → implementation → verification workflow while routing Lynx framework truth to official Lynx sources and replacing DOM-oriented component assumptions with Lynx-native `lynx-ui` guidance.

Lynx quick-start tooling can create a Lynx project and output Lynx/Web bundles, but complete native, mobile, desktop, or web host applications require host integration. For host/container claims, agents must consult official Lynx resources such as `lynx-docs://react/start/quick-start.md` and `lynx-docs://react/start/integrate-with-existing-apps.md` instead of implying a full host app can be generated from this plugin alone.

`@dumbooks/lynx-ui` is currently treated as a local workspace package at `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui`. It is positioned for future open source, but this plugin must not imply public registry availability, license clearance, npm publishability, or external stable support unless the package docs and proof gates say so.

## Official Lynx tooling setup references

These commands are documentation only. Do not run setup, install MCP servers, add community skills, or mutate user configuration unless the user starts a separate setup/configuration task.

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

When `lynx-docs` MCP is configured, agents should list resources and read `lynx-docs://llms.txt` first, then read the specific docs needed for the task. This plugin bundles local companion skills for the official Lynx AI skill family so those routes remain discoverable even before community skills are installed. When `lynx-devtool` MCP is configured and a device/app is connected, agents may use it for CDP-backed inspection, App commands, Open URL workflows, connector/transport troubleshooting, console/source diagnostics, interaction, trace/debug workflows, and screenshots; source code remains the mutation surface.

## OMX visual QA integration

For visual Lynx surfaces, use the strongest available loop:

- `lynx-app-builder` creates or consumes the concept and records host/container boundaries.
- The `$visual-ralph` workflow may orchestrate a reference → implementation → screenshot loop when a project-bound visual target exists.
- The `$visual-verdict` workflow compares an approved reference image with a captured Lynx screenshot and drives the next edit when visual evidence is available.
- Pixel diff evidence is secondary debug support; visual parity is not claimed without an inspected screenshot or structured verdict.

## Homepage and documentation links

The plugin homepage and repository metadata intentionally point to the plugin repository. Official Lynx documentation remains the framework source of truth and should be cited through Lynx Docs MCP resource names or official Lynx docs URLs in answers.

## Cookbook

See `docs/COOKBOOK.md` for common workflows:

- create or inspect a Lynx project/bundle,
- integrate a Lynx bundle into an existing host,
- build a polished Lynx screen with visual evidence,
- run a `$visual-ralph` / `$visual-verdict` visual iteration loop,
- compose UI with local-workspace `@dumbooks/lynx-ui`,
- debug with Lynx DevTool MCP when available,
- handle ReactLynx routing, TypeScript, testing, code splitting, external bundles, shared modules, state management, `reactlynx-use`, Habitat, DevTool diagnostics, trace workflows, and debug-info remapping,
- migrate web/shadcn-style patterns safely,
- keep Stripe/Supabase service work separated from Lynx UI surfaces.

## Dry-run evals

See `docs/EVALS.md` for prompt fixtures that define expected routing, evidence, prohibited claims, and pass/fail checks for this plugin without launching generated apps. Run `python3 scripts/check_evals.py` or the aggregate `python3 scripts/check_bundle.py` validator to check the fixture schema and required coverage terms.
