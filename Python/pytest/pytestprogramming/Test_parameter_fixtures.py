import pytest
# parameterized fixtures
@pytest.fixture(params=[0,1,2,3])
def param_data(request):
    return request.param

def test_param_data(param_data):
    assert param_data in [0,1,2,3,4]