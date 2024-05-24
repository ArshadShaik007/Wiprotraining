import pytest

@pytest.mark.parametrize("input1, input2, result",[(0,0,0),(1,2,3),(4,5,8)])
def test_addition(input1,input2,result):
    assert input1+input2==result