from text import count_lines, count_characters, count_bytes
import pytest
import requests


@pytest.fixture()
def our_temp_file(tmp_path):
    def make_temp_file(num_lines):
        file = tmp_path / "test.txt"
        lines = ""
        for line in range(num_lines):
            lines += str(line) + "\n"
        file.write_text(lines)
        return file
    return make_temp_file

@pytest.mark.parametrize("num_lines", [0, 1, 4, 9999])
def test_count_lines(our_temp_file, num_lines):
    assert count_lines(our_temp_file(num_lines)) == num_lines

def test_count_characters(our_temp_file):
    assert count_characters(our_temp_file(3)) == 6

def test_count_bytes(monkeypatch):

    class MockResponse:
        def __init__(self):
            self.content = b"asdsad"

    monkeypatch.setattr(requests, "get", lambda r: MockResponse())
    assert count_bytes("https://www.google.com") == 6