##################################################################
# Exercise 09: Majority Element
# Write a function that takes an array of numbers and returns the majority element. 
# A majority element is an element that appears more than half the time in the array.
# so [n / 2]

from typing import List


def majority_element(nums: List[int]) -> int:
    # your code here
    return None

##################################################################

def test_majority_element():
    assert majority_element([1, 5, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 5
    assert majority_element([1, 6, 1, 2, 2, 2, 3, 6, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 6
    assert majority_element([1, 6, 1, 7, 2, 2, 3, 7, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 7

if __name__ == "__main__":
    test_majority_element()