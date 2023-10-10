from area import area_of_square, area_of_rectangle
import pytest

@pytest.mark.parametrize(["input", "output"], [(1, 1), (2, 4), (0.5, 0.25), (0.2,0.04)])
def test_area_of_square_valid(input, output):
    assert area_of_square(input) == pytest.approx(output)


@pytest.mark.parametrize("length", [-2, -5, -0.8325])
def test_area_of_square_invalid_value(length):
    with pytest.raises(ValueError):
        area_of_square(length)


def test_area_of_square_invalid_type():
    with pytest.raises(TypeError):
        area_of_square("2")


@pytest.mark.parametrize("width", [1, 4, 0.4, 2.7])
@pytest.mark.parametrize("length", [1.2, 456, 0.4768, 2.27])
def test_area_of_rectangle_swap_width_length(length, width):
    assert area_of_rectangle(length, width) == pytest.approx(area_of_rectangle(width, length))
