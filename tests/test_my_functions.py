import pytest
from source.my_functions import add,divide

def test_add():
    assert add(1,2) == 3

def test_divide():
    assert divide(1,2) == 0.5
    with pytest.raises(ZeroDivisionError):
        divide(1,0)