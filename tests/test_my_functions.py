import scripts.my_functions as my_functions
import pytest


def test_add():
    result = my_functions.add(5, 10)
    
    assert result == 15
    


def test_subtract():
    result = my_functions.subtract(5, 10)
    
    assert result == -5
    


def test_multiply():
    result = my_functions.multiply(5, 10)
    
    assert result == 50
    


def test_division():
    result = my_functions.division(5, 10)
    
    assert result == 0.5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.division(10, 0)
        
        
