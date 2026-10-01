# Provenance

This repository contains sanitized historical extracts from private DentSignal development.

## Source period

The files represent an earlier telephony phase that included Twilio voice flow, callbacks, number provisioning, and related admin/setup work.

## What was preserved

- implementation shape;
- provider-facing control flow;
- callback/provisioning responsibilities;
- migration and hardening context.

## What was removed

- credentials;
- live phone numbers and provider identifiers;
- clinic/customer/patient data;
- environment-specific configuration;
- unrelated private application code.

## Claim boundary

These files prove that this implementation work existed in the project history. They do not prove that Twilio is the current provider, that the old setup remains deployable, or that any production/customer outcome followed from the code.

Historical evidence should stay historical even when a cleaner marketing story would be easier.
