# test_calculator.py
#from calculator import add, subtract

from calculator import add , subtract , fact

def test_add():
    assert add(2, 3) == 5  # This should pass

def test_subtract():
    assert subtract(5, 3) == 3 

def test_fact():
    assert fact(5) == 120
    