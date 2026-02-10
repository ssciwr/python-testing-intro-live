def area(side_length):
    if side_length < 0:
        raise ValueError("please note side_length cannot be negative")
    return side_length ** 2