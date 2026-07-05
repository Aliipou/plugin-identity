# plugin-identity

Identity-verification seam for the Decision OS / AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: interface-only (Protocol + demo stub).**

## What it does

Defines the `IdentityVerifier` seam: turn a credential (bearer token, SPIFFE SVID,
OIDC id_token) into a verified actor string the kernel understands. It answers
"who is this?", never "may they?". A `StaticVerifier` (fixed credential→actor map)
is included as a demo; real OIDC/SPIFFE verification replaces it.

## Authority

This plugin holds **no authority**. Identity in, actor out — the kernel still
decides authority for that actor.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_identity import StaticVerifier
v = StaticVerifier({"tok-abc": "agent:bot"})
v.actor_for("tok-abc")   # -> "agent:bot"
v.actor_for("nope")      # -> None
```

## Status and limitations

- **Interface only.** The shipped `StaticVerifier` is a demo, not real auth. A
  production verifier must validate signatures/issuer/audience/expiry against a
  real OIDC provider or SPIFFE trust domain — not implemented here.
