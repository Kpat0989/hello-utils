from utils import greet, add, subtract


def test_greet():
    assert greet("world") == "Hello, world!"
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
