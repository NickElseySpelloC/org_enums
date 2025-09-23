import org_enums


def test_can_import():
    assert isinstance(org_enums.__all__, tuple)
    for name in org_enums.__all__:
        getattr(org_enums, name)
