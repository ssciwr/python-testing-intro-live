from text import count_lines, count_characters
import pytest


@pytest.fixture()
def our_temp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("line 1\nline 2\nline 3")
    return file


def test_count_lines(our_temp_file):
    assert count_lines(our_temp_file) == 3

def test_count_characters(our_temp_file):
    assert count_characters(our_temp_file) == 21