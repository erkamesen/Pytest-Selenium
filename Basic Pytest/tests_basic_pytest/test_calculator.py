import pytest




def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def division(a, b):
    return a/b


def multiplication(a, b):
    return a*b


# TESTS
@pytest.mark.nameofmark
def test_addition():
    assert addition(2, 2) == 4

@pytest.mark.smoke
def test_subtraction():
    assert subtraction(7, 2) == 5


@pytest.mark.skip(reason="Form & CSS changed")
def test_division():
    assert division(100, 10) == 10


@pytest.mark.xfail(reason="Its expired")
def test_multiplication():
    assert multiplication(7, 5) == 36
