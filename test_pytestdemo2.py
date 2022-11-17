import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method it is executed")
    yield
    print("Once after every method")

def testMethod1(setup):
    print("This is test Method1")

def testMethod2(setup):
    print("This is test method2")