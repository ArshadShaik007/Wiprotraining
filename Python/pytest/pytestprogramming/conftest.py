import pytest

@pytest.fixture(scope='function') #use function scope to see the changes
def openclosedb():
    print("connected to database")
    yield
    print("disconnected to database")

@pytest.fixture(scope='function') #use function scope to see the changes
def openclosebrowser():
    print("opening browser")
    yield
    print("closing browser")