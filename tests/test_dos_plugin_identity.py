from dos_plugin_identity import IdentityVerifier, StaticVerifier


def test_verifier_maps_known_and_rejects_unknown():
    v = StaticVerifier({"tok-abc": "agent:bot"})
    assert isinstance(v, IdentityVerifier)
    assert v.actor_for("tok-abc") == "agent:bot"
    assert v.actor_for("nope") is None
