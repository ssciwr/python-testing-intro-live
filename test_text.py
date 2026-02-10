from text import count_lines

def test_count_lines(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("line 1\nline 2\nline 3")
    assert count_lines(file) == 3