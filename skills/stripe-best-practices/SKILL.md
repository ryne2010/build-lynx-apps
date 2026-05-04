---
name: stripe-best-practices
description: Optional service-domain guidance for Stripe integrations used by Lynx.js apps. Guides API selection, Checkout Sessions, PaymentIntents, Connect, subscriptions, and migrations while keeping payment surfaces separate from Lynx UI implementation guidance.
---

Before implementing Stripe code, check official Stripe documentation for the current API version and SDK. Do not rely on copied version notes unless verified for the target project.

## Scope for Build Lynx Apps

Use this skill for payment architecture and backend/service integration decisions. Do not treat Stripe-hosted or embedded payment surfaces as `@dumbooks/lynx-ui` components. Route Lynx app UI composition back to `lynx-app-builder` and `lynx-ui-guidance`.

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
