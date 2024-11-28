def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())