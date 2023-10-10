def area_of_square(length):
    if length < 0:
        raise ValueError("Length must be non-negative")
    return length*length


def area_of_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length must be non-negative")
    return length*length