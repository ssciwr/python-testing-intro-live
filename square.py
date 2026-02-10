def area(side_length):
    return area_rectangle(side_length, side_length)


def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("please note length and width cannot be negative")
    return length * width