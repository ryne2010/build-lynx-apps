# Image Gen Briefing for Lynx App Concepts

Use this reference when generating concept images for Lynx.js app surfaces.

## Brief requirements

Include:

- app purpose and audience,
- target device class and orientation,
- primary screen and required states,
- navigation model,
- data fields and content hierarchy,
- expected Lynx/ReactLynx implementation constraints,
- `@dumbooks/lynx-ui` component families or token mood when relevant,
- verification plan: Lynx DevTool screenshot comparison when available, static evidence otherwise.

## Concept quality bar

- Produce complete screens, not isolated hero fragments.
- Keep text and controls readable enough for implementation.
- Use Lynx-native interaction expectations rather than DOM-specific affordances.
- Make loading, empty, error, and selected states explicit when they are part of the requested flow.
- Avoid unsupported claims about native stability unless proof evidence exists.

## Implementation notes to extract

After a concept is accepted, extract:

- colors and token intent,
- typography scale,
- spacing and density,
- reusable component families,
- navigation and state model,
- motion/transition intent,
- visual QA evidence required before sign-off.
