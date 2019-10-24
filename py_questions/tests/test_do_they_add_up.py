# Do they add up tests
from questions import do_they_add_up


def test_yes_do_they_add_up():
    l1 = [4, 7, 1, -3, 2]
    add_up = do_they_add_up.do_they_add_up(l1, 5)
    assert add_up


def test_no_do_they_add_up():
    l1 = [4, 7, 1, -3, 2]
    add_up = do_they_add_up.do_they_add_up(l1, 349)
    assert not add_up
