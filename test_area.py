from area import area_of_square


def test_area_of_square():
    assert area_of_square(1) == 1
    assert area_of_square(2) == 4
    assert area_of_square(0.5) == 0.25