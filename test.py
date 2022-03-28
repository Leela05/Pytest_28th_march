import Prgm1

def test_1():
    x = 20

    result = Prgm1.square(x)
    assert result == x*x

def test_2():
    x = 20
    y = 10
    result = Prgm1.perimeter_of_rectangle(x, y)
    assert result == 2(x+y)

def test_3():
    x = 20
    y = 10
    result = Prgm1.area_of_rectangle(x, y)
    assert result == x*y
