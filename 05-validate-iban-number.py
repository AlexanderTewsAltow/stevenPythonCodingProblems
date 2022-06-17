##################################################################
# Exercise 5: Validate IBAN
# Write a function that takes an IBAN and returns True if it is valid and False otherwise.
#
# (Hint) you can find the algorithm for the IBAN validation here:
# https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
# (Hint 2) do not forget to strip away the whitespaces from the input string

# 1. Länge überprüfen
# 2. erste vier Zeichen ans Ende setzen, alle Buchstaben zu Zahlen (Format A=10, B=11, etc) konvertieren
# 3. erhaltene Zahl vollständig um 97 dividieren, wenn 1 rauskommt ist richtig

import math
from operator import mod
from timeit import repeat


def validateIBAN(iban: str) -> bool:
    strippedIban = iban.replace(" ", "")

    countries = {
        "DE": 22,
        "NL": 18
    }

    ibanDict = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35
    }
    if len(strippedIban) != countries[strippedIban[0:2]]:
        print("False - length incorrect for",iban,", given length:", len(strippedIban))
        return False

    # better method more than likely available
    firstFourChars = strippedIban[0:4]
    newIban = strippedIban[4::]
    newIban += firstFourChars
    newIban = list(newIban)

    for i in range(len(newIban)):
        if newIban[i] in ibanDict:
            newIban[i] = str(ibanDict[newIban[i]])

    newIban = "".join(newIban)

    if int(newIban) % 97 != 1:
        print("False - digit test failed for", iban)
        return False

    print("Validated IBAN", iban)
    return True
    pass

##################################################################

def test_validateIBAN():
    assert validateIBAN('NL91ABNA0417164300') == True
    assert validateIBAN('NL91 ABNA 0417 1643 00') == True
    assert validateIBAN('DE89 3704 0044 0532 0130 00') == True
    assert validateIBAN('DE89 3704 0044 0532 0130 01') == False

if __name__ == '__main__':
    test_validateIBAN()