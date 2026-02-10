from square import area, area_rectangle
import pytest


def test_area_valid():
    assert area(2) == 4
    assert area(0.5) == pytest.approx(0.25)
    assert area(0.2) == pytest.approx(0.04)


@pytest.mark.parametrize("length", [-2, -1, -0.23423, -0.00001])
def test_area_negative(length):
    with pytest.raises(ValueError) as exc_info:
        area(length)
    assert "negative" in str(exc_info.value).lower()


def test_area_string():
    with pytest.raises(TypeError):
        area("1")

@pytest.mark.parametrize(["length", "width", "output"], [(1,2,2), (0.5, 0.1,0.05)])
def test_area_rectangle_valid(length, width, output):
    assert area_rectangle(length, width) == pytest.approx(output)