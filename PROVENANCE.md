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
- unrelated private application code;
- surrounding dependency/client wiring that belonged to the larger private service.

## Non-standalone boundary

This public repository is **not** an exported runnable DentSignal service.

The Python files are historical slices. For example, the admin-route extract preserves the route surface while the surrounding authentication, clinic persistence/CRUD, configuration, and client-injection layers remain private. Other extracts likewise depend on context that was intentionally not republished.

That means syntax/compile checks are useful publication checks, but they do not establish end-to-end runnability. No missing wiring has been reconstructed here simply to make the evidence pack look like a modern demo.

## Claim boundary

These files support the claim that the published implementation work existed in the project history. They do not prove that Twilio is the current provider, that the old setup remains deployable, that the full private system is represented here, or that any production/customer outcome followed from the code.

The commit hashes cited in the public evidence are provenance references into private project history; they are not publicly inspectable substitutes for the sanitized artifacts published here.

Historical evidence should stay historical even when a cleaner marketing story would be easier.
