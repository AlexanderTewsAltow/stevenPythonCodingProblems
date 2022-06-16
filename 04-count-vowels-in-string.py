##################################################################
# Exercise 4: Count Vowels in a String
# Write a function that takes a string and returns the number of vowels in that string.

def countVowels(string: str) -> int:
    # WRITE CODE HERE
    pass

##################################################################

def test_countVowels():
    assert countVowels('abcde') == 5
    assert countVowels('abcdee') == 6
    assert countVowels('aeiou') == 5
    assert countVowels('aeiouy') == 6
    assert countVowels('') == 0

if __name__ == '__main__':
    test_countVowels()