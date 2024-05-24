import pytest

@pytest.mark.skip
def testcase1():
    print("testcase 1")

# test case 2
@pytest.mark.xfail
def testcase2():
    print("testcase 2")

# test case 3
@pytest.mark.xpass
def testcase3():
    print("testcase 3")

# test case 4
def testcase4():
    print("testcase 4")
