import pytest

system = "test"



def perimeter_of_triangle(a, b, c):
    return a+b+c


def area_of_triangle(a, h):
    return (a*h)/2


# TESTS

@pytest.fixture()
def triangle():
    print("Triangle Created")
    yield
    print("Triangle Destroyed")


@pytest.mark.skipif(condition=system=="dev", reason=("system must be test"))
def test_perimeter_of_triangle(triangle):
    assert perimeter_of_triangle(3, 5, 7) == 15

@pytest.mark.smoke
@pytest.mark.nameofmark
def test_area_of_triangle(triangle): # pytest -vm "smoke and nameofmark"
    assert area_of_triangle(5,10) == 25
    
""" 
test_triangle.py::test_perimeter_of_triangle Triangle Created
PASSEDTriangle Destroyed

test_triangle.py::test_area_of_triangle Triangle Created
PASSEDTriangle Destroyed
"""