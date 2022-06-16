##################################################################
# Exercise 1: Radians to Degrees
# Write a function that converts an angle in radians to degrees.
import math
def radiansToDegrees(radians):
    return (180/math.pi)*radians

##################################################################
def test_radiansToDegrees():
    assert radiansToDegrees(0) == 0
    assert radiansToDegrees(math.pi) == 180

if __name__ == '__main__':
    test_radiansToDegrees()
