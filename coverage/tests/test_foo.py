# test_foo.py
import foo
import pytest

def test_foo():
    expected = 1
    assert expected == foo.foo()
    return

