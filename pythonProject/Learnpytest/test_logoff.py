import pytest

def testlogin():
    print("login successfully")

def testlogoff():
    print("logoff successfully")
@pytest.mark.sanity
def testcalculation():
    assert 2+2 == 4