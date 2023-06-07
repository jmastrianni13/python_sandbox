# test__main__.py
import src.__main__ as main

def test_main_get_total():
    x = 3
    y = 4
    assert 7 == main.get_total(3, 4)
    return

