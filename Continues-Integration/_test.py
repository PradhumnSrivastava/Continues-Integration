import pytest

#function to test square
def square(n):
    return n ** 2

#function to test cube
def cube(n):
    return n ** 3

#function to test fifth power
def fifth_power(n):
    return n ** 5

#testing the square function
def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(3) == 9, "Test failed: square(3) should be 9"
    assert square(4) == 16, "Test failed: square(4) should be 16"

#testing the cube function
def test_cube():
    assert cube(2) == 8, "Test failed: cube(2) should be 8"
    assert cube(3) == 27, "Test failed: cube(3) should be 27"
    assert cube(4) == 64, "Test failed: cube(4) should be 64"
    
#testing the fifth power function

def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed: fifth_power(2) should be 32"
    assert fifth_power(3) == 243, "Test failed: fifth_power(3) should be 243"
    assert fifth_power(4) == 1024, "Test failed: fifth_power(4) should be 1024"
    
#test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("String")
    with pytest.raises(TypeError):
        cube("b")
    with pytest.raises(TypeError):
        fifth_power("c")