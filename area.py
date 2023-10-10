def area_of_square(length):
    if length < 0:
        raise ValueError("Length must be non-negative")
    return length*length