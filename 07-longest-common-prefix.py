##################################################################
# Exercise 7: Longest common prefix
# Write a function that takes a list of strings and returns the longest common prefix.
# If there is no common prefix, return an empty string "".

from typing import List

def longestCommonPrefix(strings: List[str]) -> str:
    # WRITE CODE HERE
    pass

##################################################################

def test_longestCommonPrefix():
    assert longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert longestCommonPrefix(['dog', 'racecar', 'car']) == ''
    assert longestCommonPrefix(['', 'a', 'ab']) == ''

if __name__ == '__main__':
    test_longestCommonPrefix()