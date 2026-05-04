---
name: lynx-ui-guidance
description: Use read-only @dumbooks/lynx-ui guidance for Lynx-native UI composition, component selection, registry checks, package-import-first usage, proof gates, guarded CLI boundaries, and migration planning. Applies when a Lynx app needs components, tokens, forms, overlays, patterns, themes, or a replacement for DOM-oriented UI-kit assumptions.
---

# Lynx UI Guidance

Use this skill when composing UI for Lynx.js apps with `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui` or package imports from `@dumbooks/lynx-ui`.

## Hard boundaries

- Read the local `lynx-ui` package only; do not write to it without separate explicit user approval.
- Prefer package imports from `@dumbooks/lynx-ui` for promoted internal-beta components.
- Treat `@dumbooks/lynx-ui/experimental` as an opt-in compatibility alias, not the default recommendation.
- Do not read secrets, tokens, private registry credentials, or arbitrary files outside approved project paths.
- Do not perform MCP-driven installs or writes. Install-like requests should return a guarded local CLI plan.
- Do not copy DOM/Radix/Tailwind/daisyUI runtime source into Lynx runtime code. Adapt behavior with Lynx primitives and independently authored package APIs.
- Keep proof and stability caveats visible: internal-beta, public-web-beta, and tri-platform-stable are separate proof levels.

## Registry-first component selection

Before recommending a component or migration:

1. Read the registry entry or component docs from `packages/lynx-ui`.
2. Check status, stability, ownership, public export, export channel, engine/runtime proof, proof artifacts, proof requirements, AI usage hints, and license/originality notes.
3. Prefer package imports for package-owned components.
4. For copy/install-style requests, explain the dry-run-first CLI workflow and require explicit `--write` before mutation. Do not mutate through MCP or through this skill.
5. Run the lightest validation that proves the claim; require host runtime or visual proof before UI-quality/stability claims.

Useful read-only references:

- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/README.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/AI_TOOLING_CONTRACT.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/docs/COMPONENT_REFERENCE.md`
- `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui/src/registry/manifest.json`

## Current public categories

Use registry/docs to confirm exact availability, but the current component reference groups useful UI work into:

- **Primitives:** text, surfaces, buttons, cards, badges, status, loading, separators, and foundations.
- **Forms:** fields, labels, input controls, search, selection, validation messages, toggles, sliders, and related controls.
- **Interactions:** tabs, disclosures, overlays, menus, popovers, dialogs, drawers, tooltips, carousels, pagination, and scroll/command-like surfaces.
- **Patterns:** breadcrumbs, record lists, detail sections, empty states, metric cards, workspace sections, toolbars, sidebars, tables, charts, and app-composition helpers.

## Recommended output shape

When answering UI requests:

1. State the chosen `@dumbooks/lynx-ui` import path.
2. Name the registry/doc evidence checked.
3. List proof caveats before broad quality claims.
4. Provide source changes only in the consuming app, not inside `packages/lynx-ui`, unless the user explicitly approves a package edit.
5. For unavailable components, suggest a Lynx-native composition with existing primitives/patterns and mark any missing package capability as a follow-up.
