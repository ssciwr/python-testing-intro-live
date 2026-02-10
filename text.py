def count_lines(file):
    with open(file) as f:
        return len(f.readlines())

def count_characters(file):
    with open(file) as f:
        return len(f.read())