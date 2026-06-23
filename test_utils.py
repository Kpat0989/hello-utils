from utils import greet, add


def test_greet():
    assert greet("world") == "Hello, world!"
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
