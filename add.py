def add(a, b):
    return a+b 

#pytest
def test_add():
    assert add(1, 1) == 2
def test_add2():
    assert add(1, 2) == 3


if(__name__=="_)main__"):
    print(add(1, 2))
