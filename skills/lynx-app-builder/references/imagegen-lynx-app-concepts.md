# Image Gen Briefing for Lynx App Concepts

Use this reference with the installed `imagegen` skill when `lynx-app-builder` needs an overall visual concept. This is guidance, not a prompt template; write a natural design-director brief tailored to the task.

## Must include

Copy concrete details from the user request, screenshots, existing app, or plan. Do not reduce them to a generic category like "mobile app" or "clean dashboard."

- **Scope:** complete Lynx page, complete app screen, dashboard, editor/tool surface, flow state set, or coordinated state/detail concepts.
- **Target host:** iOS, Android, HarmonyOS, Web, Windows, macOS, Lynx Explorer, or planning-only. Include viewport/screen size, density, orientation, safe-area assumptions, and desktop/window variant when known.
- **Purpose and audience:** what the surface helps the user do, who it is for, what decision/action the screen optimizes, and the product mood to convey.
- **Exact visible content:** headings, labels, CTA text, nav items, table fields, statuses, chart labels, form labels, empty/error text, sample entities, and realistic data density. Prefer user-provided content over invented filler.
- **Structure:** app shell, route/surface, sidebars, rails, drawers, overlays, lists, tables, charts, media areas, forms, footer/status regions, and responsive/device continuation.
- **State atlas:** default, loading, empty, error, selected, disabled, pressed/focused, validation, confirmation, offline/host-service-unavailable, and permission-denied states when relevant.
- **Interaction model:** selected states, filters, tabs, form editing, success state, scroll/gesture/animation behavior, and what should be main-thread responsive.
- **Visual system:** palette mood, typography personality, UI chrome/control text scale, density, spacing rhythm, radii, shadows, borders, container model, icon style, image treatment, and token mood.
- **Asset and icon plan:** required images, placeholders, avatars, thumbnails, brand marks, chart glyphs, inline SVG, external SVG `src`, local asset names, and fallback visuals if assets are unavailable.
- **Content hierarchy:** primary path, secondary actions, destructive/irreversible actions, status severity, progressive disclosure, and how dense information should be grouped.
- **Accessibility and i18n cues:** touch target scale, contrast intent, truncation/wrapping, locale-sensitive copy/number/date lengths, and non-color status cues.
- **Lynx implementation constraints:** code-native `page`/`view`/`text`/`image`/`svg`/`scroll-view`/`list` UI, CSS Modules, global tokens only for theme layers, host-safe assets, and no browser/DOM-only controls.
- **Local UI package direction:** if `@dumbooks/lynx-ui` is relevant, ask for component families and tokens compatible with the local-workspace package; do not ask imagegen to invent exact package APIs.
- **Verification plan:** Lynx DevTool screenshot comparison when available; `$visual-verdict` when a reference and screenshot exist; static/build evidence otherwise.

## Quality bar

Every concept should feel like a professional product mockup by a senior product designer:

- Complete requested surface, not a header-only crop.
- Clear product point of view and coherent IA.
- Readable text and controls that can be implemented as code-native Lynx UI.
- Excellent typography, including buttons, tabs, inputs, sidebars, table cells, labels, and other control chrome.
- Coherent palette, spacing, radius, border, elevation, icon treatment, asset handling, and chart/metric language.
- Practical Lynx-native component anatomy and state coverage.
- Purposeful motion/gesture cues only where they clarify state.
- Dense areas shown at production density with enough detail to implement without guessing.
- Explicit mobile/desktop differences when the target host or viewport changes.
- No browser-default fallback visuals, DOM-specific affordances, fake metrics, unsupported host/service claims, inaccessible contrast, or ambiguous placeholder blobs.

## Visual-direction guardrails

When the user does not provide a complete visual system, choose a coherent direction instead of returning generic UI:

- Pick one primary visual metaphor or product personality, then make color, spacing, shadows, iconography, and interaction states support it.
- Use token-friendly values: semantic colors, neutral scales, radius scale, elevation model, font-size/line-height rhythm, and spacing increments that can be represented in CSS Modules/tokens.
- Prefer Lynx-friendly layouts: flex/grid-like regions, scroll/list boundaries, cards/surfaces, section headers, and explicit text wrappers.
- Avoid fine browser-only affordances such as DOM focus rings, HTML controls, CSS hover-only interactions, web scrollbars, or Radix-specific overlay anatomy unless the target is explicitly Lynx for Web and caveated.
- For charts, maps, and diagrams, describe implementable shapes, labels, legends, axes, series colors, empty/error states, and whether SVG or composed Lynx views are intended.

## Image count and clarity

- For a single simple screen, one primary concept may be enough.
- For a complex dashboard, editor, list/detail flow, or form-heavy surface, generate the full primary screen plus focused detail/state concepts for dense areas.
- For stateful flows, include loading, empty, error, selected, confirmation, and disabled states when relevant.
- For responsive or cross-host work, generate separate mobile and desktop/window concepts instead of implying one screenshot proves all hosts.
- For dense tables/lists/forms/charts, request standalone zoomed detail concepts with legible copy and component anatomy.
- If any concept screenshot is too small, blurry, cropped, or ambiguous, generate a fresh standalone detail/state concept instead of cropping or guessing.

## After generation

Extract before coding:

- visible-copy lock,
- state atlas and state-to-component mapping,
- Lynx element inventory,
- route/app-shell architecture,
- colors and token intent,
- typography scale,
- spacing and density,
- radius/border/elevation model,
- reusable component families,
- `@dumbooks/lynx-ui` component candidates and unavailable/fallback components,
- asset manifest and icon/SVG treatment,
- navigation and state model,
- motion/transition intent and main-thread responsiveness candidates,
- accessibility/i18n considerations,
- host services/native modules implied by the concept,
- visual QA evidence required before sign-off.

If `$visual-ralph` will own implementation, save the approved reference in the workspace and carry forward viewport, route/state, asset manifest, and interaction parity notes.
