from app import add, is_positive


def test_add():
    assert add(2, 3) == 5


def test_is_positive():
    assert is_positive(5) is True


def test_negative_number_is_not_positive():
    assert is_positive(-1) is False
