##################################################################
# Exercise 6: Calculate prime numbers
# Write a function that takes a number (the amount) and returns a list of all prime numbers up to that number.
#
# (Hint) you can find what a prime number is here:
# https://en.wikipedia.org/wiki/Prime_number

def calculatePrimeNumbers(number: int) -> list[int]:
    # WRITE CODE HERE
    pass

##################################################################

def test_calculatePrimeNumbers():
    assert calculatePrimeNumbers(10) == [2, 3, 5, 7]
    assert calculatePrimeNumbers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert calculatePrimeNumbers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

if __name__ == '__main__':
    test_calculatePrimeNumbers()