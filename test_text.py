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


def make_file(temp_path, text):
    filename = temp_path / "tmp.txt"
    print(filename)
    with open(filename, "w") as f:
        f.write(text)
    return filename


def test_our_text(tmp_path):
    filename = make_file(tmp_path, "our text")
    assert count_lines(filename) == 1


@pytest.fixture
def make_file_fixture(tmp_path):
    def _callable(text):
        filename = tmp_path / "tmp.txt"
        print(filename)
        with open(filename, "w") as f:
            f.write(text)
        return filename
    return _callable


def test_our_text2(make_file_fixture):
    filename = make_file_fixture("our text")
    assert count_lines(filename) == 1


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
        def __init__(self):
            self.content = b"abc"

    monkeypatch.setattr(requests, "get", lambda _: FakeRequestsObject())

    url = "sdgfsd"
    assert count_bytes(url) == 3