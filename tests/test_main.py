from project import add


def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(2, 0) == 2
