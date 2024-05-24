import pytest

def setup_module(moodule):
    print("opening the db connection")


def teardown_module(module):
    print("closing the db connection")

def testcase1():
    print("testcase 1")

# test case 2
def testcase2():
    print("testcase 2")

# test case 3
def testcase3():
    print("testcase 3")
