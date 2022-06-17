##################################################################
# Exercise 3: Decimal to Binary
# Write a function that takes a number and returns a string with the binary representation of that number.

import math

# % is decimal
# // round
def decimalToBinary(number):
    string = ""
    while True:
        if number % 2 == 0:
            string += "0"
        else:
            string += "1"
        number = number//2

        if number == 0:
            return string[::-1]

##################################################################

def test_decimalToBinary():
    assert decimalToBinary(0) == '0'
    assert decimalToBinary(1) == '1'
    assert decimalToBinary(2) == '10'
    assert decimalToBinary(42) == '101010'

if __name__ == '__main__':
    test_decimalToBinary()