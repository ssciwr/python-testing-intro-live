from area import area_of_square
import pytest


def test_area_of_square_valid():
    assert area_of_square(1) == 1
    assert area_of_square(2) == 4
    assert area_of_square(0.5) == 0.25
    assert area_of_square(0.2) == pytest.approx(0.04)


def test_area_of_square_invalid_value():
    with pytest.raises(ValueError):
        area_of_square(-2)
    with pytest.raises(ValueError):
        area_of_square(-5)


def test_area_of_square_invalid_type():
    with pytest.raises(TypeError):
        area_of_square("2")