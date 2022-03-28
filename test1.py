import Divisible

def test_5():
    x = 20
    result = Divisible.divisible_by_5(x)
    assert result == True


def test_7():
    x = 28
    result = Divisible.divisible_by_7(x)
    assert result == True

def test_9():
    x = 20
    result = Divisible.divisible_by_9(x)
    assert result == False



def test_10():
    x = 20
    result = Divisible.divisible_by_10(x)
    assert result == True


