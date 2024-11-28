import requests

def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

def count_chars(filename):
    with open(filename) as f:
        return len(f.read())

def count_bytes(url):
    response = requests.get(url)
    return len(response.content)