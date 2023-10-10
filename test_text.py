from text import count_lines, count_characters
import pytest


@pytest.fixture
def temp_filename(tmp_path):
    filename = tmp_path / "tmp.txt"
    print(filename)
    with open(filename, "w") as f:
        f.write("hello")
    return filename


@pytest.fixture
def long_temp_filename(temp_filename):
    with open(temp_filename, "w+") as f:
        f.write("\nworld")
    return temp_filename


def test_count_lines(temp_filename):
    assert count_lines(temp_filename) == 1


def test_count_characters(temp_filename):
    assert count_characters(temp_filename) == 5


def test_count_lines_long(long_temp_filename):
    assert count_lines(long_temp_filename) == 2
