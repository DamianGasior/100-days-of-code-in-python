import calculator
import pytest

def test_add():
    assert calculator.add(2,3)==5
    assert calculator.add(-1,1)==0


def test_subtract():
    assert calculator.subtract(5,3)==2
    assert calculator.subtract(-1,-2)==1


def multiply():
    assert calculator.multiply(10,3)==30
    assert calculator.multiply(0,3)==0

def test_divide():
    assert calculator.divide(30,3)==10

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10,0)

@pytest.mark.parametrize("a,b,result",[
    (2,3,5),
    (-1,1,0),
    (0,0,0)
    ])

def test_add(a,b,result):
    assert calculator.add(a,b)==result
