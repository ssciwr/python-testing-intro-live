from area import area_of_square
import pytest

def test_area_of_square():
    assert area_of_square(1) == 1
    assert area_of_square(2) == 4
    assert area_of_square(0.5) == pytest.approx(0.25)
    assert area_of_square(0.2) == pytest.approx(0.04)


@pytest.mark.parametrize("length", [-1, -2, -4.66])
def test_area_of_square_negative_inputs(length):
    with pytest.raises(ValueError) as e:
        area_of_square(length)
    assert "negative" in str(e.value).lower()

def test_area_of_rectangle_swap_length_width_gives_same_area():
    assert area_of_rectangle(2, 3) == area_of_rectangle(3, 2)