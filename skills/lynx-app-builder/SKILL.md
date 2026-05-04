---
name: lynx-app-builder
description: Use for new Lynx.js apps, ReactLynx screens, dashboards, product surfaces, mobile flows, and visually driven Lynx UI from scratch or redesign. Builds from high-quality image-generated concepts, routes framework truth through official Lynx tooling, composes UI with Lynx-native guidance, and verifies with Lynx DevTool screenshots or explicit static/build evidence.
---

# Lynx App Builder

Use this skill to create polished Lynx.js app surfaces. Act first as a product designer, then as a Lynx implementation engineer, then as an evidence-focused verifier.

## Core standard

1. Create enough great-looking concept design first when the task is visual, unless the user opts out or the change is a small fix inside an existing design system.
2. Implement faithfully from the accepted concept using Lynx/ReactLynx constraints, official Lynx docs, and `lynx-ui` guidance when appropriate.
3. Verify with the strongest evidence available. Prefer Lynx DevTool MCP screenshot/interaction/console/source evidence when configured and connected; otherwise run static/build/lint checks and clearly state that visual parity was not proven.

## Required routing before implementation

- For Lynx framework/API/build behavior, use `lynx-official-tools` and current official docs. If `lynx-docs` MCP is configured, read `lynx-docs://llms.txt` first.
- For component and token choices, use `lynx-ui-guidance` and read local registry/docs before recommending package APIs.
- For payment or data-layer work, use the optional service skills only after the Lynx UI and framework boundaries are clear.
- Do not run official MCP/community-skill setup commands unless the user explicitly requests setup mode.

## Design workflow

Before generating concepts:

- Capture the product purpose, audience, required screens/states, navigation, data fields, copy, motion needs, target device classes, and verification constraints.
- Ask for complete app surfaces: primary screen, key states, empty/loading/error states, and any needed responsive or device-specific variations.
- Prefer concept images that make text, controls, spacing, and component anatomy readable. Regenerate unclear sections instead of implementing from ambiguous references.
- Avoid generic filler, invented product claims, unsupported platform affordances, and DOM-only interaction assumptions.

After concept acceptance:

- Extract design tokens: color, type scale, spacing, radii, elevation, icon treatment, motion cues, and component families.
- Map repeated UI elements to `@dumbooks/lynx-ui` components or Lynx-native compositions.
- Preserve information architecture and visible copy unless the user approves a change.

## Implementation workflow

1. Detect existing project conventions and Lynx/ReactLynx setup before writing code.
2. Read current official Lynx docs for any uncertain framework/build/runtime behavior.
3. Prefer `@dumbooks/lynx-ui` root imports for internal-beta package components when registry/docs support the target surface.
4. Keep source changes in the consuming app. Do not edit `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui` without explicit approval.
5. Avoid browser globals, DOM-specific event assumptions, Radix/browser-only primitives, and uncontrolled UI-kit ports.
6. Keep service integrations separate from UI composition; Stripe and Supabase guidance is optional service-domain help, not UI implementation guidance.

## Verification workflow

Use the strongest available evidence tier:

### Tier 1 — Lynx visual evidence

Use when Lynx DevTool MCP is configured, a device/app is connected, and screenshots/interactions are available.

- Inspect the running Lynx page with DevTool MCP.
- Capture screenshot evidence.
- Use `view_image` and, when useful, `$visual-verdict` to compare the accepted concept and latest screenshot.
- Do not finish while meaningful visual, layout, state, or interaction mismatches remain.

### Tier 2 — Static/runtime evidence without screenshots

Use when DevTool/device preview is unavailable.

- Run available project checks: typecheck, lint, build, unit tests, component checks, or static validation.
- Report that visual parity is not proven because screenshot evidence was unavailable.
- Do not use visual-signoff language.

### Tier 3 — Planning-only evidence

Use when the user only asks for guidance or when no project exists yet.

- Provide setup steps, file map, official docs routing, and verification plan.
- Do not claim implemented behavior.

## Optional visual orchestration

Use `$visual-ralph` or `$visual-verdict` only when there is an actual visual target and screenshot/reference evidence. They add value for measured visual scoring, not for purely static skill/documentation edits.

## Completion checklist

- Official Lynx docs or MCP resources used for framework claims.
- `lynx-ui` registry/docs checked for component claims.
- No setup side effects unless explicitly requested.
- No `lynx-ui` package writes without explicit approval.
- Verification evidence is named by tier.
- No visual parity claim without screenshot evidence.
