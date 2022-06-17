##################################################################
# Exercise 7: Longest common prefix
# Write a function that takes a list of strings and returns the longest common prefix.
# If there is no common prefix, return an empty string "".

from typing import List

def longestCommonPrefix(strings: List[str]) -> str:
    # jeweils den anfangsbuchstaben überprüfen, wenn 1. gleich ist -> 2. überprüfen, wenn 2. gleich ist -> nächsten, usw
    commonPrefix = ""
    checkedWords = 0
    amountWords = len(strings)

    for words in strings:
        if words == "":
            return ""

    while checkedWords != amountWords - 1:
        if strings[checkedWords][checkedWords] == strings[checkedWords + 1][checkedWords]:
            commonPrefix += strings[checkedWords][checkedWords]
        else:
            checkedWords = amountWords
            break
        checkedWords += 1

    return commonPrefix

##################################################################

def test_longestCommonPrefix():
    assert longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert longestCommonPrefix(['dog', 'racecar', 'car']) == ''
    assert longestCommonPrefix(['', 'a', 'ab']) == ''

if __name__ == '__main__':
    test_longestCommonPrefix()