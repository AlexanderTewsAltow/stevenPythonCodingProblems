##################################################################
# Exercise 5: Validate IBAN
# Write a function that takes an IBAN and returns True if it is valid and False otherwise.
#
# (Hint) you can find the algorithm for the IBAN validation here:
# https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
# (Hint 2) do not forget to strip away the whitespaces from the input string

def validateIBAN(iban: str) -> bool:
    # WRITE CODE HERE
    pass

##################################################################

def test_validateIBAN():
    assert validateIBAN('NL91ABNA0417164300') == True
    assert validateIBAN('NL91 ABNA 0417 1643 00') == True
    assert validateIBAN('DE89 3704 0044 0532 0130 00') == True
    assert validateIBAN('DE89 3704 0044 0532 0130 01') == False

if __name__ == '__main__':
    test_validateIBAN()