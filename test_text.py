from text import count_lines
import pytest

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "file.txt"
    with open(temp_file, "w") as f:
        f.write("Hello")
    return temp_file

def test_count_lines(temp_file):
    assert count_lines(temp_file) == 2