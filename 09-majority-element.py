##################################################################
# Exercise 09: Majority Element
# Write a function that takes an array of numbers and returns the majority element. 
# A majority element is an element that appears more than half the time in the array.
# so [n / 2]

from tabnanny import check
from typing import List

#Liste durchgehen, erste Nummer als curMajority setzen und count + 1, wenn nächste Nummer ungleich des curMajority, 1 vom count abnehmen, sonst count + 1, wenn count = 0 bei nächster Nummer
#dann nächste Nummer als curMajority setzen und count + 1
def majority_element(nums: List[int]) -> int:
    curMajority = None
    count = 0

    for n in nums:
        if (curMajority == None) or (curMajority != n and count == 0):
            curMajority = n
            count += 1
        elif (curMajority != n and count >= 1):
            count -= 1
        elif curMajority == n:
            count += 1
    print(curMajority)
    return curMajority

##################################################################

def test_majority_element():
    assert majority_element([1, 5, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 5
    assert majority_element([1, 6, 1, 2, 2, 2, 3, 6, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 6
    assert majority_element([1, 6, 1, 7, 2, 2, 3, 7, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 7

if __name__ == "__main__":
    test_majority_element()