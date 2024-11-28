from area import area_of_square
import pytest

def test_area_of_square():
    assert area_of_square(1) == 1
    assert area_of_square(2) == 4
    assert area_of_square(0.5) == pytest.approx(0.25)
    assert area_of_square(0.2) == pytest.approx(0.04)


def test_area_of_square_invalid():
    with pytest.raises(ValueError) as e1:
        area_of_square(-1)
    with pytest.raises(ValueError) as e2:
        area_of_square(-2)
    assert "negative" in str(e2.value).lower()
    with pytest.raises(TypeError):
        area_of_square("3")