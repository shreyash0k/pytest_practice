import pytest
from source.my_functions import add,divide

def test_add():
    result = add("i like ","cola")
    assert result == "i like cola"

def test_divide():
    assert divide(1,2) == 0.5
    with pytest.raises(ZeroDivisionError):
        divide(1,0)