def area_of_square(side):
    return area_of_rectangle(side, side)

def area_of_rectangle(width, length):
    if width < 0 or length < 0:
        raise ValueError("width and length must be non-negative")
    return width * length