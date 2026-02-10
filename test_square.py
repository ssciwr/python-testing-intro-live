from square import area
import pytest


def test_area_valid():
    assert area(2) == 4
    assert area(0.5) == pytest.approx(0.25)
    assert area(0.2) == pytest.approx(0.04)