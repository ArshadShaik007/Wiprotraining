import pytest
# test case 1
@pytest.mark.sanity
def testcase1():
    print("testcase 1")

# test case 2
@pytest.mark.regression
def testcase2():
    print("testcase 2")

# test case 3
@pytest.mark.sanity
def testcase3():
    print("testcase 3")

# test case 4
@pytest.mark.regression
def case_Test():
    print("testcase 4")

# test case 5
@pytest.mark.sanity
def login():
    print("loging in")