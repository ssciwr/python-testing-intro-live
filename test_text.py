from text import count_lines

def test_count_lines(tmp_path):
    temp_file = tmp_path / "file.txt"
    with open(temp_file, "w") as f:
        f.write("Hello\nWorld")
    assert count_lines(temp_file) == 2