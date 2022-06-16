##################################################################
# Exercise 1: Radians to Degrees
# Write a function that converts an angle in radians to degrees.

def radiansToDegrees(radians):
    # WRITE CODE HERE
    pass

##################################################################
def test_radiansToDegrees():
    assert radiansToDegrees(0) == 0
    assert radiansToDegrees(0.5) == 0.927295
    assert radiansToDegrees(1) == 1.5707963267948966
    assert radiansToDegrees(1.5) == 2.6179938779914944
    assert radiansToDegrees(2) == 3.141592653589793

if __name__ == '__main__':
    test_radiansToDegrees()
