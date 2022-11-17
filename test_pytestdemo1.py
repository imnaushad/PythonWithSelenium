import pytest

@pytest.fixture()
def setup():
    print("Once before every method it is executed")

def testMethod1(setup):
    print("This is test Method1")

def testMethod2(setup):
    print("This is test method2")