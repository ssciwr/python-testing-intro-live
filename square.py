def area(side_length):
    if side_length < 0:
        raise ValueError("please note side_length cannot be negative")
    return side_length ** 2


def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("please note length and width cannot be negative")
    return length * width