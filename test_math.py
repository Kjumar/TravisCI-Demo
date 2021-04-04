import my_math

def test_addition():
    assert my_math.add(1, 2) == 3, "Should be 3"

def test_subtraction():
    assert my_math.subtract(1, 5) == -4, "Should be -1"

def test_multiplication():
    assert my_math.multiply(2, 4) == 8, "Should be 8"

def test_divide():
    assert my_math.divide(6, 3) == 2, "Should be 2"
