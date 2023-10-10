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

@pytest.mark.parametrize("width", [1, 4, 0.4, 2.7])
def test_area_of_rectangle_swap_width_length(length, width):
    assert area_of_rectangle(length, width) == pytest.approx(area_of_rectangle(width, length))
