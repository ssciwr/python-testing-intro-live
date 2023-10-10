from text import count_lines

@pytest.fixture
def temp_filename(tmp_path):
    filename = tmp_path / "tmp.txt"
    print(filename)
    with open(filename, "w") as f:
        f.write("hello")
    return filename

def test_count_lines(tmp_path):
    assert count_lines(filename) == 1