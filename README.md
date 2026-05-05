# Build Lynx Apps Plugin

Builder workflows for Lynx.js app surfaces, pages, projects, and bundles that route to official global Lynx tooling, use local-workspace UI composition with `@dumbooks/lynx-ui`, support measured OMX visual QA loops, and include optional app-service integration guidance.

## Skills

This plugin intentionally keeps a small local skill surface. Official Lynx AI skills and MCP servers are **not vendored here**; install them globally from the official Lynx sources and let agents route to them when Lynx framework truth, DevTool runtime inspection, trace analysis, TypeScript, or ReactLynx best-practice guidance is needed.

- `lynx-app-builder` — concept-first Lynx surface workflow with implementation inventories, OMX visual orchestration, and evidence-based verification.
- `lynx-ui-guidance` — read-only local-workspace `@dumbooks/lynx-ui` usage guidance, package-import-first component selection, proof gates, official-substrate metadata, local/internal-beta caveats, and guarded CLI boundaries.
- `stripe-best-practices` — optional service-domain guidance for payment flows used by Lynx app surfaces.
- `supabase-postgres-best-practices` — optional service-domain guidance for Postgres/Supabase data layers used by Lynx app surfaces.

### Official Lynx prerequisites

For current Lynx documentation, DevTool runtime inspection, and the upstream Lynx AI skill set, install the official tools globally rather than from this repository:

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

These commands are documentation only for this plugin. Do not run setup, install MCP servers, add community skills, or mutate user configuration unless the user starts a separate setup/configuration task.

## Install and distribution

This repository supports the current `gh skill` path for installing individual Agent Skills. It also includes Codex plugin marketplace metadata so the repository can be added as a Codex plugin marketplace source.

Public readiness status:

- GitHub repository: public at `https://github.com/ryne2010/build-lynx-apps`.
- Current plugin version: `0.1.1` in `.codex-plugin/plugin.json`.
- Latest release tag to publish: `v0.1.1`.
- Release state: `v0.1.0` is published; `v0.1.1` is the next release candidate for the latest core-doc updates.

As the sole maintainer, validate locally first, then publish a tagged release only when you are ready.

### Install individual skills with GitHub CLI

Install a specific skill for Codex at user scope:

```bash
gh skill install ryne2010/build-lynx-apps lynx-app-builder --agent codex --scope user
```

Preview skills before installing:

```bash
gh skill preview ryne2010/build-lynx-apps
gh skill preview ryne2010/build-lynx-apps lynx-ui-guidance
```

Search for published/discoverable skills from this owner:

```bash
gh skill search lynx --owner ryne2010
```

Install other bundled skills by name, for example:

```bash
gh skill install ryne2010/build-lynx-apps lynx-ui-guidance --agent codex --scope user
gh skill install ryne2010/build-lynx-apps stripe-best-practices --agent codex --scope user
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
python3 scripts/check_evals.py
gh skill publish --dry-run .
```

Versioning uses SemVer in `.codex-plugin/plugin.json` and immutable Git tags named `vMAJOR.MINOR.PATCH`.

Automatic publishing:

- Pushes to `main` run `.github/workflows/publish-skills.yml` only when release-relevant files change: plugin metadata, marketplace metadata, root agent metadata, assets, skill files, release docs/evals, validators, license, or the workflow itself.
- The workflow derives the release tag from `.codex-plugin/plugin.json` as `v<version>`.
- The workflow validates the bundle, eval fixtures, and `gh skill publish --dry-run .` before publishing.
- If the derived tag already exists, validation fails with a version-bump error so release-relevant pushes cannot silently pass with a skipped publish job.
- Validation runs with `contents: read`; the final publish job alone gets `contents: write` so `gh skill publish --tag ... .` can create the GitHub release/tag.
- The workflow pins `actions/checkout` to a full commit SHA (`v4.2.2`) instead of a mutable tag.
- The workflow asserts GitHub CLI support for `gh skill` (`gh >= 2.90.0`) and, if the runner is too old, installs pinned GitHub CLI `2.92.0` after verifying the downloaded `.deb` SHA-256.
- Repository releases are immutable, and the `versioning` ruleset protects `v*` tags by restricting deletions and blocking force pushes.

Release checklist:

1. Update `.codex-plugin/plugin.json` `"version"` to the intended SemVer value.
2. Update this README so the current plugin version and next release tag match that value.
3. Run the local validators and `gh skill publish --dry-run .`.
4. Commit the release-ready bundle.
5. Publish with the matching `v<version>` tag.

When ready to publish a new version, create the tagged GitHub release through `gh skill publish`:

```bash
gh skill publish --tag v0.1.1
```

Do not run the non-dry-run publish command until the intended tag, README, skill metadata, and repository contents are final. Keep the GitHub tag-protection ruleset in place so published versions remain immutable.

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

`@dumbooks/lynx-ui` is currently treated as a local workspace package at `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui`. It is positioned for future open source, but this plugin must not imply public registry availability, license clearance, npm publishability, or external stable support unless the package docs and proof gates say so. If the target app cannot resolve the local package, agents should provide a Lynx-native fallback using official Lynx elements and CSS Modules instead of suggesting public installation.

### Lynx UI availability, exports, and examples

Agents must re-check the local package manifest before making package-consumer claims. If `packages/lynx-ui/package.json` still marks the package private, unlicensed, repo-local, unpublished, or otherwise not externally consumable, guidance remains local-workspace/internal-beta only.

When local package resolution is proven, use the exact export surface from the package manifest rather than invented paths:

  - `@dumbooks/lynx-ui`
  - `@dumbooks/lynx-ui/tokens`
  - `@dumbooks/lynx-ui/tokens.css`
  - `@dumbooks/lynx-ui/token-registry`
  - `@dumbooks/lynx-ui/flavors`
  - `@dumbooks/lynx-ui/registry`
  - `@dumbooks/lynx-ui/registry-manifest`
  - `@dumbooks/lynx-ui/experimental` — compatibility alias only, not the default recommendation

Before writing component usage, read the registry entry and its registry examples when present. The quickest local examples are under `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/examples/`, especially `components.tsx` for root component composition and `flavor-gallery.tsx` for visual style/base-color/token usage.

## Official Lynx tooling setup references

These commands are documentation only. Do not run setup, install MCP servers, add community skills, or mutate user configuration unless the user starts a separate setup/configuration task.

```bash
codex mcp add lynx-docs -- npx @lynx-js/docs-mcp-server@latest
codex mcp add lynx-devtool -- npx @lynx-js/devtool-mcp-server@latest
npx skills add lynx-community/skills
```

When `lynx-docs` MCP is configured, agents should list resources and read `lynx-docs://llms.txt` first, then read the specific docs needed for the task. This plugin does not bundle local companion copies of the official Lynx AI skill family. When `lynx-devtool` MCP is configured and a device/app is connected, agents may use it for CDP-backed inspection, App commands, Open URL workflows, connector/transport troubleshooting, console/source diagnostics, interaction, trace/debug workflows, and screenshots; source code remains the mutation surface.

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
- compose UI with local-workspace `@dumbooks/lynx-ui`, including exact export-surface and registry examples checks,
- debug with Lynx DevTool MCP when available,
- handle ReactLynx routing, TypeScript, testing, code splitting, external bundles, shared modules, state management, `reactlynx-use`, Habitat, DevTool diagnostics, trace workflows, and debug-info remapping,
- migrate web/shadcn-style patterns safely,
- keep Stripe/Supabase service work separated from Lynx UI surfaces.

## Dry-run evals

See `docs/EVALS.md` for prompt fixtures that define expected routing, evidence, prohibited claims, and pass/fail checks for this plugin without launching generated apps. Run `python3 scripts/check_evals.py` or the aggregate `python3 scripts/check_bundle.py` validator to check the fixture schema and required coverage terms.
