# test_bar.py
import bar
import pytest

def test_bar():
    expected = 2
    assert expected == bar.bar()
    return

