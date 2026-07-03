"""Identity verification seam (OAuth2 / OIDC / SPIFFE workload identity).

INTERFACE ONLY. Turns a credential (bearer token, SVID) into a verified actor
string the kernel understands. It answers 'who is this?', never 'may they?'.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class IdentityVerifier(Protocol):
    scheme: str

    def actor_for(self, credential: str) -> str | None:
        """Return a verified actor id, or None if the credential is invalid."""
        ...


class StaticVerifier:
    """Demo verifier: a fixed credential->actor map. Real OIDC/SPIFFE replaces it."""

    scheme = "static"

    def __init__(self, table: dict[str, str] | None = None) -> None:
        self._t = table or {}

    def actor_for(self, credential: str) -> str | None:
        return self._t.get(credential)
