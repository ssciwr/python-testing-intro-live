from text import count_lines


def test_count_lines(tmp_path):
    filename = tmp_path / "tmp.txt"
    with open(filename, "w") as f:
        f.write("hello")
    assert count_lines(filename) == 1