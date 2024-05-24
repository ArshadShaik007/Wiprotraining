import pytest

def setup_function(function):
    print("opening the browser")


def teardown_function(function):
    print("closing the browser")

def testcase1():
    print("testcase 1")

# test case 2
def testcase2():
    print("testcase 2")

# test case 3
def testcase3():
    print("testcase 3")
