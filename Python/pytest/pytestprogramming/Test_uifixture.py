import pytest



@pytest.mark.usefixtures("openclosebrowser")
def test_login():
    print("username")
    print("password")
    print("click to login")

@pytest.mark.usefixtures("openclosebrowser")
def test_logout():
    print("user logged out")