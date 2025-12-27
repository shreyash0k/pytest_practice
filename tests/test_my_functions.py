import pytest
from source.my_functions import add,divide
from source.shapes import Square

@pytest.mark.skip(reason="in progress feature")
def test_add():
    result = add("i like ","cola")
    assert result == "i like cola"

@pytest.mark.xfail(reason="we can not divide by zero")
def test_divide():
    assert divide(1,0) == 0

@pytest.mark.parametrize("side_length,expected_area",[(4,16),(3,9)])
def test_area(side_length,expected_area):
    sqr = Square(side_length)
    assert sqr.area() == expected_area

