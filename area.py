def area_of_square(side):
    if side < 0:
        raise ValueError("side must be non-negative")
    return side * side

def area_of_rectangle(width, length):
    if width < 0 or length < 0:
        raise ValueError("width and length must be non-negative")
    return width * length