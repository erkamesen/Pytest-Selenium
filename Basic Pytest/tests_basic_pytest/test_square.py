import pytest

def perimeter_of_square(a):
    return 4*a


def area_of_square(a):
    return a*a


# TESTS

def test_perimeter_of_square():
    print("this function calculate to perimeter of the square")
    assert perimeter_of_square(4) == 16 # pytest -vs

@pytest.mark.nameofmark
def test_area_of_square(): # pytest -m nameofmark
    assert area_of_square(2) == 4


