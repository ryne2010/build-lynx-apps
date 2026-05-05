---
name: stripe-best-practices
description: Optional service-domain guidance for Stripe integrations used by Lynx.js apps. Guides API selection, Checkout Sessions, PaymentIntents, Connect, subscriptions, and migrations while keeping payment surfaces separate from Lynx UI implementation guidance.
---

Before implementing Stripe code, check official Stripe documentation for the current API version and SDK. Do not rely on copied version notes unless verified for the target project.

## Scope for Build Lynx Apps

Use this skill for payment architecture and backend/service integration decisions. Do not treat Stripe-hosted or embedded payment surfaces as `@dumbooks/lynx-ui` components. Route Lynx app UI composition back to `lynx-app-builder` and `lynx-ui-guidance`.


## Lynx host/client safety

When Stripe is used by a Lynx app surface, keep payment architecture separate from Lynx UI composition:

- Do not put Stripe secret keys, webhook secrets, restricted keys, ephemeral key minting secrets, or PaymentIntent/Checkout privileged creation logic in a Lynx bundle.
- Create Checkout Sessions, PaymentIntents, SetupIntents, subscriptions, Connect accounts, and webhook handlers on a trusted backend.
- Treat Lynx surfaces as clients that display state, collect allowed user intent, and hand off to hosted/native/web payment surfaces documented by Stripe and the target host.
- Verify current Stripe docs and SDK/API versions before writing code; payment rules are temporally sensitive.
- Record the target host surface (native app, web host, embedded web surface, or backend-only flow) before recommending Checkout, Payment Element, native handoff, or webhook architecture.
- Do not treat Stripe-hosted or embedded payment UI as `@dumbooks/lynx-ui` components. Compose only the surrounding Lynx-native product UI.
- For PCI/security claims, cite official Stripe docs and clearly separate planning guidance from launch/legal/compliance approval.

## Integration routing

| Building... | Recommended API | Details |
|---|---|---|
| One-time payments | Checkout Sessions | [references/payments.md](references/payments.md) |
| Custom payment form or externally hosted payment surface | Checkout Sessions or Payment Element | [references/payments.md](references/payments.md) |
| Saving a payment method for later | Setup Intents | [references/payments.md](references/payments.md) |
| Connect platform or marketplace | Accounts v2 (`/v2/core/accounts`) | [references/connect.md](references/connect.md) |
| Subscriptions or recurring billing | Billing APIs + Checkout Sessions | [references/billing.md](references/billing.md) |
| Embedded financial accounts / banking | v2 Financial Accounts | [references/treasury.md](references/treasury.md) |

Read the relevant reference file before answering any integration question or writing code.

## Key documentation

When the user's request does not clearly fit a single domain above, consult:

- [Integration Options](https://docs.stripe.com/payments/payment-methods/integration-options.md) — Start here when designing any integration.
- [API Tour](https://docs.stripe.com/payments-api/tour.md) — Overview of Stripe's API surface.
- [Go Live Checklist](https://docs.stripe.com/get-started/checklist/go-live.md) — Review before launching.
