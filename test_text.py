from text import count_lines
import pytest


@pytest.fixture()
def our_temp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("line 1\nline 2\nline 3")


def test_count_lines(our_temp_file):
    assert count_lines(our_temp_file) == 3