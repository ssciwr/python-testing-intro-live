from text import count_lines, count_characters, count_bytes
import pytest
import requests


@pytest.fixture
def temp_filename(tmp_path):
    filename = tmp_path / "tmp.txt"
    print(filename)
    with open(filename, "w") as f:
        f.write("hello")
    return filename


@pytest.fixture
def long_temp_filename(temp_filename):
    with open(temp_filename, "a") as f:
        f.write("\nworld")
    return temp_filename


def test_count_lines(temp_filename):
    assert count_lines(temp_filename) == 1


def test_count_characters(temp_filename):
    assert count_characters(temp_filename) == 5


def test_count_lines_long(long_temp_filename):
    assert count_lines(long_temp_filename) == 2


def test_count_bytes(monkeypatch):

    class FakeRequestsObject:
        def __int__(self):
            self.content = b"abc"
    url = "https://github.com/ssciwr/python-testing-intro-live/raw/main/README.md"
    assert count_bytes(url) == 260