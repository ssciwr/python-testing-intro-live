import requests

def count_lines(file):
    with open(file) as f:
        return len(f.readlines())

def count_characters(file):
    with open(file) as f:
        return len(f.read())

def count_bytes(url):
    response = requests.get(url)
    return len(response.content)