---
name: lynx-ui-guidance
description: Use read-only @dumbooks/lynx-ui guidance for Lynx-native UI composition, component selection, registry checks, package-import-first usage, exact export surface and examples lookup, proof gates, official-substrate metadata, guarded CLI boundaries, local-workspace/external-consumer framing, and migration planning. Applies when a Lynx app needs components, tokens, forms, overlays, patterns, themes, visual styles, base colors, or a replacement for DOM-oriented UI-kit assumptions.
license: MIT
---

# Lynx UI Guidance

Use this skill when composing UI for Lynx.js apps with the local workspace package at `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui` or package imports from `@dumbooks/lynx-ui` inside this workspace.

This package is poised for future open source, but this skill must frame it as **local to the current workspace for now**. Do not imply public npm availability, public OSS release approval, license clearance, or external consumer stability unless the local package docs/manifest and release proofs explicitly say so.

This skill is a read-time contract checklist. Do not hardcode component counts, stability counts, or schema assumptions from remembered docs; query the local registry/docs/CLI/MCP surface available in the current environment because docs and manifest can diverge.

## Hard boundaries

- Read the local `lynx-ui` package only; do not write to it without a separate explicit package-edit task.
- Treat `@dumbooks/lynx-ui` as a local-workspace/internal-beta dependency unless the consuming project evidence proves a published package source.
- Prefer package imports from `@dumbooks/lynx-ui` for promoted internal-beta package components when the consuming workspace can resolve the local package.
- Treat `@dumbooks/lynx-ui/experimental` as an opt-in compatibility alias, not the default recommendation.
- Do not read secrets, tokens, private registry credentials, or arbitrary files outside approved project paths.
- Do not perform MCP-driven installs or writes. Install-like requests should return a guarded local CLI plan.
- Do not copy DOM/Radix/Tailwind/daisyUI runtime source into Lynx runtime code. Adapt behavior with Lynx primitives and independently authored package APIs.
- Keep proof and stability caveats visible: `internal-beta`, `public-web-beta`, and `tri-platform-stable` are separate proof levels.
- Keep app business logic outside design-system migration suggestions: preserve route-owned calculations, navigation targets, data selectors, and service boundaries.

## Local-workspace framing

When recommending `@dumbooks/lynx-ui`:

- State that the evidence comes from the local workspace path unless the target app already declares a resolvable package dependency.
- Do not claim it is published, installable from a public registry, or stable for unrelated external projects.
- If the target app is outside the Dumbooks/workspace context, provide two paths: local workspace integration if available, or a Lynx-native composition fallback using official Lynx elements and CSS Modules.
- Separate internal package import proof from external package-consumer proof. Source aliases, workspace app runtime proof, and built package proof are not interchangeable.
- Future OSS readiness is a roadmap/status note, not permission to copy package source or make public release claims.

## External-consumer availability gate

For any target app that is outside the local Dumbooks/workspace context, first check whether `@dumbooks/lynx-ui` is actually consumable by that app:

1. Read the target app's dependency graph (`package.json`, workspace config, lockfile, aliases, or package manager workspace evidence) for a resolvable `@dumbooks/lynx-ui` dependency.
2. Read `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/package.json` for `private`, `license`, `version`, `exports`, peer dependencies, and package files before making availability claims.
3. If the package manifest is still private, unlicensed, repo-local, or otherwise unpublished, state that package-import guidance is local-workspace/internal-beta only and give a Lynx-native fallback composition.
4. Built package claims require built-dist proof such as `pnpm validate:lynx-ui:package-build`; public registry or public OSS claims require explicit package manifest, release, license/originality, and publication evidence.
5. Do not suggest `npm install @dumbooks/lynx-ui`, public registry installation, external support expectations, or native-stable quality unless the current package evidence proves those claims.

## Registry-first component selection

Before recommending a component, import path, migration, stability claim, copy/install plan, or visual-style/base-color choice:

1. Read the registry entry, local docs, registry examples, or MCP component resource from `packages/lynx-ui`.
2. Check these required fields when present in the manifest/resource:
   - `status`
   - `stability`
   - `ownership.copyInstall`
   - `publicExport`
   - `exportChannel`
   - `engineCompatibility.proof`
   - `runtimeCompatibility.proofGate`
   - `runtimeCompatibility.targetHosts`
   - `runtimeCompatibility.verifiedHosts`
   - `sourceProvenance`
   - `contentHash`
   - `proofArtifacts`
   - `proofRequirements`
   - `aiUsageHints`
   - `licenseOriginalityNotes`
   - `officialSubstrateStatus`
   - `officialSubstrate`
   - `adapterStrategy`
   - `dependencyGate`
3. Check the registry `examples` field and the referenced `examples/*.tsx` files when usage patterns, prop combinations, state ownership, or visual-style/base-color composition are needed. Do not invent component APIs when an example or docs file exists.
4. Prefer package imports for package-owned components whose `exportChannel` supports root package use and whose workspace resolution is available.
5. Keep official substrate status visible:
   - `official-backed` means an approved official Lynx UI package or facade is part of the implementation.
   - `official-concept-complete` means official concepts inform the local implementation without an unapproved runtime dependency.
   - `local-owned-complete` means local tokens/elements/proof gates own the behavior.
   - unresolved/deferred substrate or dependency gates must be reported as follow-up risk, not hidden.
6. For copy/install-style requests, explain the dry-run-first CLI workflow and require explicit write-mode approval before mutation. Do not mutate through MCP or through this skill.
7. Run or request the lightest validation that proves the claim; require host runtime or visual proof before UI-quality/stability claims.

## Useful read-only references

- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/package.json`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/README.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/AI_TOOLING_CONTRACT.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/COMPONENT_REFERENCE.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/COMPONENT_STRATEGY.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/OFFICIAL_LYNX_UI_HYBRID_STRATEGY.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/src/registry/manifest.json`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/src/index.ts`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/examples/README.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/examples/components.tsx`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/examples/flavor-gallery.tsx`

## Package, source-alias, and proof distinctions

- The root `@dumbooks/lynx-ui` entrypoint is the default recommendation for internal-beta package components when the registry says the component is publicly exported through the root channel and the consuming workspace can resolve it.
- `@dumbooks/lynx-ui/experimental` is a compatibility alias for promotion-history consumers and future opt-in experimental entries; do not recommend it by default.
- Workspace app runtime proof can be source-alias scoped. Do not treat source-alias behavior as proof that built package artifacts work for external package consumers.
- Built package claims require package-build proof such as `pnpm validate:lynx-ui:package-build` in the `lynx-ui` repo; do not run it unless the user is working in that repo and asks for validation.
- Public/external runtime claims require built-dist package proof or a future host-runtime proof that consumes built artifacts.
- Public web beta and tri-platform stable are separate release profiles; internal beta does not imply public release approval, iOS/Android proof, or native-stable quality.
- License/originality notes and public OSS release gates must stay visible when adapting shadcn-like, daisyUI-like, or official-substrate concepts.

## Exact export surface

Confirm the current `package.json` `exports` map before recommending imports. As of the current local package contract, the intended import surfaces are:

- `@dumbooks/lynx-ui` — root internal-beta component and token entrypoint; default only when workspace/package resolution is proven.
- `@dumbooks/lynx-ui/tokens` — token helpers and registries for code consumers.
- `@dumbooks/lynx-ui/tokens.css` — token/theme CSS side-effect import for theme layers.
- `@dumbooks/lynx-ui/token-registry` — token registry JSON for tooling/inspection.
- `@dumbooks/lynx-ui/flavors` — visual style and base-color registries.
- `@dumbooks/lynx-ui/registry` — registry helper module for local tooling.
- `@dumbooks/lynx-ui/registry-manifest` — registry manifest JSON for read-only metadata checks.
- `@dumbooks/lynx-ui/experimental` — compatibility alias only; never the default recommendation.

If any export is missing, private, source-alias-only, or blocked by the target workspace, do not invent an import path. Report the missing exact export surface and provide a Lynx-native fallback using official elements and CSS Modules.

## Examples-first usage lookup

When usage is unclear, read examples before writing or recommending code:

- Prefer a component registry `examples` field when present because it is component-scoped.
- Use `examples/components.tsx` for root component composition patterns.
- Use `examples/flavor-gallery.tsx` for visual style/base-color/token composition.
- Use workflow-specific examples such as `examples/reconciliation-exception-review.tsx` when forms, validation messages, review queues, or app-local business logic boundaries are in scope.
- Treat examples as usage evidence, not permission to copy private package internals into external projects. Preserve route-owned business logic and adapt only public-safe package imports or Lynx-native composition patterns.

## Local CLI boundary

Use these as documentation or read-only planning guidance, not as implicit permission to mutate:

```bash
pnpm lynx-ui list --json
pnpm lynx-ui info <component-id> --json
pnpm lynx-ui theme --json
pnpm lynx-ui list --items --json
pnpm lynx-ui doctor --json
pnpm lynx-ui check --json
pnpm lynx-ui diff <component-id> --to <target-dir> --json
```

`diff` is read-only. `add`, `copy`, `install`, and `sync` are dry-run by default in the package contract; mutating runs require explicit `--write`, a caller-provided target directory, generated-file markers, rollback/provenance metadata, and conflict guards. This skill must not run those mutating commands unless the user starts a separate approved copy/install task.

## Current public categories

Use registry/docs to confirm exact availability. Do not hardcode counts.

- **Primitives:** text, surfaces, buttons, cards, badges, status, loading, separators, and foundations.
- **Forms:** fields, labels, input controls, search, selection, validation messages, toggles, sliders, and related controls.
- **Interactions:** tabs, disclosures, overlays, menus, popovers, dialogs, drawers, tooltips, carousels, pagination, and scroll/command-like surfaces.
- **Patterns:** breadcrumbs, record lists, detail sections, empty states, metric cards, workspace sections, toolbars, sidebars, tables, charts, and app-composition helpers.
- **Platform items:** visual styles, base-color palettes, token/theme layer, CLI, MCP, docs, registry, and skill metadata via `list --items`, the manifest `items` array, or local docs.

## Recommended output shapes

### Component recommendation

1. State the chosen `@dumbooks/lynx-ui` import path and that it is local-workspace/internal-beta unless target evidence proves otherwise.
2. State the exact export surface used, including subpath when relevant.
3. Name the registry/doc/example evidence checked.
4. List package availability and proof caveats before broad quality/stability claims.
5. State `officialSubstrateStatus`, `officialSubstrate`, `adapterStrategy`, and `dependencyGate` when relevant.
6. Provide source changes only in the consuming app, not inside `packages/lynx-ui`, unless the user starts a package-edit task.
7. If workspace resolution or external-consumer proof is not proven, include a Lynx-native fallback composition using official elements and CSS Modules.

### Unavailable component

1. State that the component was not found or lacks the required proof/export/workspace gate.
2. Suggest a Lynx-native composition using available primitives/patterns or official elements.
3. Mark missing package capability as a follow-up instead of inventing a package API.

### Copy/install request

1. Prefer package import first when local workspace resolution is available.
2. If copy ownership is explicitly required, return a dry-run plan using `pnpm lynx-ui diff <id> --to <dir> --json`.
3. Explain that mutation requires a separate explicit `--write` command and review of generated rollback/provenance metadata.
4. Do not perform MCP writes.

### Visual style/base color selection

1. Query theme/style/base-color metadata (`theme`, `list --items`, registry `items`, docs, or MCP resource).
2. State selected visual style and base-color evidence.
3. Record proof limits for the target host before making visual-quality claims.

### Migration guidance

1. Preserve business logic, navigation, data selectors, accounting/service behavior, and host/native-module boundaries.
2. Replace DOM/Radix/Tailwind runtime assumptions with Lynx elements, CSS Modules, tokens, and package APIs.
3. Keep unavailable capabilities as follow-ups and require validation evidence before broad stability claims.
4. Separate local-workspace import guidance from future OSS/package-release guidance.
