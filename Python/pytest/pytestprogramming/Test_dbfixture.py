import pytest
@pytest.mark.usefixtures("openclosedb")
def test_create():
    print("table is created")

@pytest.mark.usefixtures("openclosedb")
def test_delete():
    print("table is deleted")

@pytest.mark.usefixtures("openclosedb")
def test_select():
    print("table is selected")