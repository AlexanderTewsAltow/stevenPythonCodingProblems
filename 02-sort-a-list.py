##################################################################
# Exercise 2: Sort a List of numbers
# Write a function that takes a list of numbers and returns a new list with the numbers sorted in ascending order.

from unittest import skip


def sortList(numbers):
    
    # 1. gehen über die liste
    # 2. curr small wird auf index gesetzt
    # 3. nochmal über liste gehen (an index anfangen) -> wenn zahl kleiner als currSmallest dann curSmallest = index dieser Zahl
    # 4. switch mit index & currentSmallest, und index+=1
    for j in range(0, len(numbers)):
        for i in range(j, len(numbers)):
            if numbers[i] < numbers[j]:
                switch(numbers, j, i) 

    return numbers

def switch(numbers, firstIndex: int, secondIndex: int):
    tmp = numbers[firstIndex]
    numbers[firstIndex] = numbers[secondIndex]
    numbers[secondIndex] = tmp

    return numbers

##################################################################

def test_sortList():
    print(sortList([5, 4, 3, 2, 1]))
    assert sortList([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sortList([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sortList([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert sortList([]) == []

if __name__ == '__main__':
    test_sortList()