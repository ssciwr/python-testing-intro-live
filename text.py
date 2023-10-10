import requests


def count_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return len(lines)


def count_characters(filename):
    with open(filename) as f:
        lines = f.readlines()
    # sum = 0
    # for line in lines:
    #    sum = sum + len(line)
    return sum(len(line) for line in lines)


def count_bytes(url):
    return len(requests.get(url).content)