from square import area
import pytest


def test_area_valid():
    assert area(2) == 4
    assert area(0.5) == pytest.approx(0.25)
    assert area(0.2) == pytest.approx(0.04)

def test_area_negative():
    with pytest.raises(ValueError) as exc_info:
        area(-2)
    assert "negative" in str(exc_info.value).lower()
    with pytest.raises(ValueError) as exc_info:
        area(1)
    assert "negative" in str(exc_info.value).lower()