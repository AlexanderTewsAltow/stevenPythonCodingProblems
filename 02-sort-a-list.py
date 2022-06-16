##################################################################
# Exercise 2: Sort a List of numbers
# Write a function that takes a list of numbers and returns a new list with the numbers sorted in ascending order.

def sortList(numbers):
    # WRITE CODE HERE
    pass

##################################################################

def test_sortList():
    assert sortList([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sortList([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sortList([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert sortList([]) == []

if __name__ == '__main__':
    test_sortList()