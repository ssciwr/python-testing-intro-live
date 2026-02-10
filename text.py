def count_lines(file):
    with open(file) as f:
        return len(f.readlines())