import pytest

def square(num):
    return num**2

@pytest.mark.parametrize (" input1, result ",[(0,0),(1,3),(4,16)])
def test_square(input1,result):
    assert square(input1) == result