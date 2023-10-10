from text import count_lines
import pytest


@pytest.fixture
def temp_filename(tmp_path):
    filename = tmp_path / "tmp.txt"
    print(filename)
    with open(filename, "w") as f:
        f.write("hello")
    return filename


def test_count_lines(temp_filename):
    assert count_lines(temp_filename) == 1