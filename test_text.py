from text import count_lines, count_chars, count_bytes
import pytest
import requests

@pytest.fixture()
def temp_file(tmp_path):
    temp_file = tmp_path / "file.txt"
    with open(temp_file, "w") as f:
        f.write("Hello\nWorld")
    return temp_file

def test_count_lines(temp_file):
    assert count_lines(temp_file) == 2

def test_count_chars(temp_file):
    assert count_chars(temp_file) == 11

def test_count_bytes(monkeypatch):
    class MockResponse:
        self.content = b"Hi"

    assert count_bytes("http://www.google.com") == 2