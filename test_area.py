from area import area_of_square, area_of_rectangle
import pytest


def test_area_of_square_valid():
    assert area_of_square(1) == 1
    assert area_of_square(2) == 4
    assert area_of_square(0.5) == 0.25
    assert area_of_square(0.2) == pytest.approx(0.04)


@pytest.mark.parametrize("length", [-2, -5, -0.8325])
def test_area_of_square_invalid_value(length):
    with pytest.raises(ValueError):
        area_of_square(length)


def test_area_of_square_invalid_type():
    with pytest.raises(TypeError):
        area_of_square("2")


def test_area_of_rectangle_swap_width_length():
    assert area_of_rectangle(1, 2) == area_of_rectangle(2, 1)