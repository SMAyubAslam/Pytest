import pytest

def testlogin():
    print("login successfully")
@pytest.mark.sanity
def testlogoff():
    print("logoff successfully")
@pytest.mark.skip
def testcalculation():
    assert 2+2 == 4
@pytest.mark.xfail
def testcalculation1():
    assert 2+2 == 4