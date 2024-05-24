import pytest

def removeG(string):
    return string.replace('g','')

@pytest.mark.parametrize (" input1, result ",
                          [
                              ('go here','o here'),('google','oole'),('good','good')
                           ])
def test_string(input1,result):
    assert removeG(input1) == result