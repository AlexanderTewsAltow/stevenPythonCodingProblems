##################################################################
# Exercise 4: Count Vowels in a String
# Write a function that takes a string and returns the number of vowels in that string.

def countVowels(string: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    index = 0
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    print(count)
    return count

##################################################################

def test_countVowels():
    assert countVowels('abcde') == 2
    assert countVowels('abcdee') == 3
    assert countVowels('aeiou') == 5
    assert countVowels('aeiouy') == 5
    assert countVowels('') == 0

if __name__ == '__main__':
    test_countVowels()