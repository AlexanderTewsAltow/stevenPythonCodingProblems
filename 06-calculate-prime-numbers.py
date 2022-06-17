##################################################################
# Exercise 6: Calculate prime numbers
# Write a function that takes a number (the amount) and returns a list of all prime numbers up to that number.
#
# (Hint) you can find what a prime number is here:
# https://en.wikipedia.org/wiki/Prime_number

import math
from typing import List


def calculatePrimeNumbers(number: int) -> List[int]:
    curNum = 1
    allNum = {}
    primeNumbers = []

    while not curNum > number:
        allNum[curNum] = [0]
        curNum += 1
    
    #wenn eine 0 rauskommt beim modulus der zahl mit einer anderen außer der sich selbst und 1 = keine primzahl
    for i in range(len(allNum)):

        for givenNum in allNum:
            staticI = i+1
            if (staticI%givenNum == 0) and givenNum != (staticI or 1):
                allNum[staticI].append(givenNum)            
    
    for numbers in allNum:
        if len(allNum[numbers]) == 2:
            primeNumbers.append(numbers)

    print(primeNumbers)
    return primeNumbers
    pass

##################################################################

def test_calculatePrimeNumbers():
    assert calculatePrimeNumbers(10) == [2, 3, 5, 7]
    assert calculatePrimeNumbers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert calculatePrimeNumbers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

if __name__ == '__main__':
    test_calculatePrimeNumbers()