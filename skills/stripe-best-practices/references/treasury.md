# Treasury / Financial Accounts

## Table of contents
- v2 Financial Accounts API
- Legacy v1 Treasury

## v2 Financial Accounts API

For embedded financial accounts (bank accounts, account and routing numbers, money movement), use the [v2 Financial Accounts API](https://docs.stripe.com/api/v2/core/vault/financial-accounts.md) (`POST /v2/core/vault/financial_accounts`). This is required for new integrations.

For Treasury concepts and guides, see the [Treasury overview](https://docs.stripe.com/treasury.md).

## Legacy v1 Treasury

Do not use the [v1 Treasury Financial Accounts API](https://docs.stripe.com/api/treasury/financial_accounts.md) (`POST /v1/treasury/financial_accounts`) for new integrations. Existing v1 integrations continue to work.


## Lynx financial-account boundary

A Lynx surface may display financial-account status and collect allowed user intent, but embedded financial-account creation, money movement, and privileged banking operations must stay on trusted backend or Stripe-supported native/host surfaces. Do not put restricted keys, account/routing-number provisioning logic, or compliance-sensitive flows directly in a Lynx bundle.
