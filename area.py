def area_of_square(side):
    if side < 0:
        raise ValueError("side must be non-negative")
    return side * side