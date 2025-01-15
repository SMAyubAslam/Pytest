import pytest

@pytest.mark.sanity
def testlogin():
    print("login successfully")

def testlogoff():
    print("logoff successfully")

def testcalculation():
    assert 2+2 == 4