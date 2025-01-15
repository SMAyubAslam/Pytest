import pytest

# @pytest.fixture(params=['a','b'])       #First Method
# def demo_fixture(request):
#     print(request.param)
#
# def testlogin(demo_fixture):
#     print("Login successfully")

@pytest.mark.parametrize('a, b, final',[(2,6,8),(5,8,15),(10,5,15)])
def testAdd(a,b,final):
    assert a+b==final