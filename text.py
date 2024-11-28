def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

def count_chars(filename):
    with open(filename) as f:
        return len(f.read())