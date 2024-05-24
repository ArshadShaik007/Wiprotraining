import pytest

@pytest.fixture
def product2(request):
    return request.param *2

@pytest.mark.parametrize("product2",[1,2,3],indirect=True)
def test_indirect_fixture(product2):
    assert product2 in [2,4,6]