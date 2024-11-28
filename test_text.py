from text import count_lines

def test_count_lines(tmp_path):
    with open(tmp_path / "file.txt", "w") as f:
        f.write("Hello\nWorld\n")
    assert count_lines(tmp_path / "file.txt") == 2