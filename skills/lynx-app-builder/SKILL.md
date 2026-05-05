---
name: lynx-app-builder
description: Use for Lynx.js app surfaces, ReactLynx screens, pages, dashboards, product surfaces, mobile flows, and visually driven Lynx UI from scratch or redesign. Builds from high-quality image-generated concepts, routes framework truth through official Lynx tooling, applies ReactLynx guardrails, composes UI with local-workspace Lynx UI guidance, and verifies with Lynx DevTool screenshots, $visual-ralph/$visual-verdict evidence, or explicit static/build evidence.
license: MIT
---

# Lynx App Builder

Use this skill to create polished Lynx.js app surfaces, pages, projects, and bundles. Act first as a product designer, then as a Lynx/ReactLynx implementation engineer, then as an evidence-focused verifier.

## Core standard

The priorities of this skill outrank convenience:

1. Create enough great-looking concept design first when the task is visual, unless the user opts out or the change is a small fix inside an existing design system.
2. Implement faithfully from the accepted concept using Lynx/ReactLynx constraints, official Lynx docs/global community-skill guidance and `lynx-ui` guidance when appropriate.
3. Verify with the strongest evidence available. Prefer Lynx DevTool MCP screenshot/interaction/console/source evidence when configured and connected; otherwise run static/build/lint/test checks and clearly state that visual parity was not proven.
4. Leave a reusable Lynx-native design system: tokens, component variants, state patterns, and verification commands that future agents can reproduce.

## Host/container boundary

- Lynx quick-start tooling can create Lynx projects and output Lynx/Web bundles.
- Complete native, mobile, desktop, or web host applications require host integration. Do not imply this plugin can build a full host app from scratch without reading official host-integration resources.
- For host/container claims, use the globally installed official Lynx Docs MCP/community skills when available and cite `lynx-docs://react/start/quick-start.md` or `lynx-docs://react/start/integrate-with-existing-apps.md` as appropriate.
- Record the target host explicitly: iOS, Android, HarmonyOS, Web, Windows, macOS, Lynx Explorer, a product host, or planning-only.
- Keep Lynx bundle work, host engine initialization, native module registration, resource loading, service injection, and app-store/native release tasks as separate workstreams.

## Required routing before implementation

- For Lynx framework/API/build/runtime behavior, use current official docs. If the globally installed `lynx-docs` MCP is configured, read `lynx-docs://llms.txt` first.
- For ReactLynx component code, events, native modules, main-thread scripts, shared modules, routing, data fetching, or TypeScript, route to the globally installed upstream Lynx community skills when available; otherwise read the matching official Lynx docs before coding.
- For component and token choices, use `lynx-ui-guidance` and read local registry/docs before recommending package APIs.
- For payment or data-layer work, use the optional service skills only after the Lynx UI and framework boundaries are clear.
- Do not run official MCP/community-skill setup commands unless the user starts a separate setup/configuration task.

## Concept design hard rules

1. Design the complete requested surface before coding. For a screen, dashboard, or flow, include the primary screen plus key loading, empty, error, selected, and interaction states.
2. For dense surfaces, generate or request separate state/detail concepts when text, controls, tables, forms, spacing, or component anatomy would be unreadable in one image.
3. Treat the accepted concept as a production design spec. Do not reinterpret visible copy, hierarchy, layout, density, container model, colors, typography, imagery, or interaction model unless the user approves or a concrete Lynx/runtime blocker requires a documented deviation.
4. Reject or iterate concepts that are header-only for a full-surface ask, generic, repetitive, over-decorated, off-product, unreadable, or dependent on DOM/browser-only affordances.
5. Preserve supplied information architecture, workflow, labels, data fields, and product claims. Do not invent unsupported metrics, navigation, or claims just to make the screen feel full.
6. Prefer concepts that are implementation-readable on the target device class: control labels, spacing, component variants, icon meaning, and typography should be extractable.
7. Keep real app UI text and controls code-native. Generated raster assets can include text only when the text belongs inside the asset itself, such as a product image, poster, logo treatment, or background sign.
8. If a Lynx target needs desktop-specific mouse, keyboard, wheel, or cursor behavior, state that it depends on official desktop support and host compatibility proof.
9. For production surfaces, require a state atlas and asset/icon plan before coding: states, SVG/image sources, host-safe asset paths, fallback visuals, accessibility/i18n cues, and responsive/device variants.

## Image Gen workflow

Use the installed `imagegen` skill when a visual task benefits from a reference image. Use `references/imagegen-lynx-app-concepts.md` for the brief shape.

Before generating a concept:

- Copy concrete requirements from the user: product purpose, audience, target host/device, route/surface, required states, visible copy, data fields, interactions, and supplied screenshots or brand constraints.
- Ask for a complete Lynx app surface or coordinated state set, not a decorative hero fragment, unless the user explicitly requested only a small slice.
- Specify Lynx implementation constraints: code-native `page`/`view`/`text`/`image`/`scroll-view`/`list` UI, CSS Modules, `rpx`/responsive sizing where useful, no browser-only affordances, no DOM widgets, and practical ReactLynx state/event behavior.
- If `@dumbooks/lynx-ui` is relevant, ask for component families and token mood that could be implemented with the local-workspace package, not for guessed package APIs.
- Ask for separate detail concepts when tables, forms, overlays, drawers, sidebars, charts, or dense control chrome would be too small to extract.
- Preserve supplied IA and data. Do not let concept generation invent unrelated routes, fake metrics, unsupported financial/medical/legal claims, or host features that the target app does not provide.
- Ask for implementation-readable asset/icon/SVG treatment, state atlas, accessibility/i18n cues, and responsive/device variants when those are relevant to the target host.

After generation:

- Reject concepts that are unreadable, off-host, impossible to implement with Lynx primitives, dependent on DOM/browser controls, or missing required states.
- Extract visible copy, layout, tokens, component anatomy, icon treatment, state model, motion/gesture intent, and unresolved details before coding.
- Extract asset manifest, SVG/image fallback plan, accessibility/i18n notes, and dense detail concepts before coding any complex surface.
- If the implementation will be measured visually, save or reference the accepted image path and carry it into the Visual QA ledger.

## Design quality bar

A strong Lynx app concept should show:

- one clear product point of view,
- intentional density for the target device class,
- complete state coverage for the requested workflow,
- excellent typography and readable control/chrome text,
- coherent palette, spacing, radius, border, elevation, and icon treatment,
- practical Lynx-native component anatomy,
- state atlas, asset/icon/SVG plan, and accessibility/i18n cues that can be implemented without guessing,
- purposeful motion or main-thread interactions only where they clarify state,
- no browser-default visual fallbacks,
- no DOM-only interaction assumptions.

Default to clean, airy, tasteful product UI: distinctive enough to feel designed, restrained enough to build and verify.

## Before coding: design and implementation inventory

Turn the accepted concept into an implementation inventory before editing source:

- Product purpose, audience, target host/device class, route/surface name, required states, data fields, and interaction paths.
- Exact visible copy, labels, navigation, CTA text, status text, form fields, table headers, chart labels, empty/error text, and important data labels.
- Design tokens: background, surface, text, muted text, border, shadow/elevation, accent, semantic colors, radii, spacing scale, typography, icon style, and motion timing.
- Component families and variants: app shell, navigation, cards/panels, forms, tables/lists, badges/status, overlays, tabs, drawers, pagination, loading/empty/error states, and responsive/device variants.
- Asset inventory: images, icons, SVG usage, logos, product illustrations, native aspect ratios, loading behavior, host-safe asset paths, and unresolved details.
- Lynx element inventory: `page`, `view`, `text`, `image`, `svg`, `scroll-view`, `list`, `input`, `textarea`, custom elements, and any host/native modules.
- Styling inventory: CSS Modules for component internals, global CSS only for token/theme layers, CSS inheritance caveats, CSS custom properties, `rpx`/responsive sizing decisions, and host-safe asset paths.
- ReactLynx inventory: event handlers, native API calls, `background only` functions, `main-thread:` interactions, refs, `runOnMainThread`, `runOnBackground`, shared modules, serializable main-thread captures, static JSX candidates, TypeScript declaration needs, and no `window`/`document`/React DOM assumptions.
- Build and bundle inventory: package manager, scripts, Rspeedy config, `engineVersion`, Lynx/Web output bundles, code splitting or external bundle needs, and whether the route is app-owned or host-loaded.
- Test inventory: unit/component tests, ReactLynx Testing Library availability, lint/typecheck/build scripts, DevTool/device preview, and visual screenshot path.
- Service boundary inventory: any Stripe/Supabase/backend/host-service work kept separate from Lynx UI composition.

If any inventory item is uncertain, retrieve official docs or local registry/docs before coding instead of guessing.

## Implementation workflow

1. Detect existing project conventions and Lynx/ReactLynx setup before writing code.
2. Read current official Lynx docs for any uncertain framework/build/runtime behavior.
3. Apply official ReactLynx guidance and any globally installed upstream Lynx community skills to component code, event handling, native modules, main-thread scripts, shared modules, static JSX, routing/data patterns, and TypeScript.
4. Prefer `@dumbooks/lynx-ui` root imports for local-workspace internal-beta package components when registry/docs support the target surface.
5. Keep source changes in the consuming app. Do not edit `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui` without a separate explicit package-edit task.
6. Avoid browser globals, DOM-specific events, React DOM assumptions, Radix/browser-only primitives, Tailwind runtime assumptions, and uncontrolled UI-kit ports.
7. Use Lynx elements and CSS Modules rather than DOM elements and browser CSS assumptions.
8. For routing, prefer official ReactLynx routing docs and memory-router-compatible patterns; do not assume browser history, `document`, or links work as they do on the web.
9. For data fetching and host data, record whether data comes from init data, global props, Fetch, Native Modules, or a backend API. Do not promise networking/storage behavior unless the host provides the service.
10. For code splitting or external bundles, verify bundle/resource paths and CSS/bundle boundaries from official Rspeedy docs before claiming reuse across apps.
11. Keep service integrations separate from UI composition; Stripe and Supabase guidance is optional service-domain help, not UI implementation guidance.
12. Preserve the accepted concept. If a Lynx limitation forces a deviation, document the blocker, cite the source, and choose the closest Lynx-native behavior.

## Visual orchestration with OMX skills

Use `$visual-ralph` when the user wants a complete visual implementation loop from a generated reference, static reference, or live URL-derived baseline. It is appropriate only when there is or will be an approved visual target.

Use `$visual-verdict` when both a reference image and a generated/current screenshot exist. Treat it as an iteration gate, not a decoration:

- Save the approved reference under a workspace artifact path such as `.omx/artifacts/visual-ralph/<slug>/reference.png` when doing project-bound visual work.
- Capture the current Lynx screenshot with recorded host/device, route/state, and viewport/screen size.
- Run `$visual-verdict` before the next visual edit; if the score is below 90, convert differences and suggestions into the next edit plan.
- Use pixel diff only as secondary debug evidence; the structured verdict remains the authoritative edit driver.
- When DevTool/device screenshots are unavailable, do not invoke visual pass/fail language. Fall back to Tier 2 static/build evidence and state that visual parity is unproven.

## Verification workflow

Use the strongest available evidence tier and name the tier in the final response.

### Tier 1 — Lynx visual/runtime evidence

Use when Lynx DevTool MCP is configured, a device/app is connected, and screenshots/interactions are available.

- Inspect the running Lynx page with DevTool MCP.
- Check console, source, element/style state, and relevant interaction paths.
- Capture screenshot evidence.
- Use `view_image` and, when useful, `$visual-verdict` to compare the accepted concept and latest screenshot.
- Do not finish while meaningful visual, layout, state, copy, or interaction mismatches remain.

### Tier 2 — Static/runtime evidence without screenshots

Use when DevTool/device preview is unavailable.

- Run available project checks: typecheck, lint, build, unit tests, ReactLynx Testing Library tests, component checks, or static validation.
- Report that visual parity is not proven because screenshot evidence was unavailable.
- Do not use visual-signoff language.

### Tier 3 — Planning-only evidence

Use when the user only asks for guidance or when no project exists yet.

- Provide setup steps, file map, official docs routing, implementation plan, and verification plan.
- Do not claim implemented behavior.

## Visual QA ledger

For visual work, track and report:

- accepted concept/reference path or prompt,
- target host/device and viewport/screen size,
- DevTool/device availability,
- screenshot artifact path or static fallback reason,
- `$visual-verdict` score/verdict when used,
- pixel diff or overlay path when used,
- states compared,
- at least five inspected comparison points for non-trivial surfaces,
- copy diff result for visible text,
- interaction path checked,
- intentional deviations with Lynx/runtime rationale,
- remaining unproven items.

## Completion checklist

- Official Lynx docs or MCP resources used for framework claims.
- ReactLynx guardrails applied for native APIs, events, main-thread work, shared modules, static JSX, routing/data patterns, and TypeScript.
- `lynx-ui` registry/docs checked for component claims.
- No setup side effects unless the user starts a separate setup/configuration task.
- No `lynx-ui` package writes without a separate explicit package-edit task.
- Verification evidence is named by tier.
- No visual parity claim without screenshot evidence or `$visual-verdict` evidence.
- Host app/container boundary is stated when relevant.
- Reusable design tokens/components and validation commands are left behind for future work.
