import pytest

def test_simple_assrt():
    assert 1+2==3

def test_equal_assert():
    assert 1==1

def test_unequal_assert():
    assert 1!=2

# verify that a value is existed in an iterable
def test_in_assert():
    assert 3 in [1,2,4,5,5]

# verify that a value is existed in an iterable
def test_not_in_assert():
    assert 4 not in [1,2,3,5,6,7]
def test_is_assert():
    a='hello world'
    b=a
    assert b is a