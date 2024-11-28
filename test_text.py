from text import count_lines, count_chars, count_bytes
import pytest
import requests

@pytest.fixture()
def temp_file(tmp_path):
    def func(n_lines):
        temp_file = tmp_path / "file.txt"
        with open(temp_file, "w") as f:
            for _ in range(n_lines):
                f.write("Hello\n")
        return temp_file
    return func

def test_count_lines(temp_file):
    assert count_lines(temp_file(2)) == 2

def test_count_chars(temp_file):
    assert count_chars(temp_file(2)) == 12

def test_count_bytes(monkeypatch):
    class MockResponse:
        content = b"Hi"

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    assert count_bytes("http://www.google.com") == len(MockResponse.content)