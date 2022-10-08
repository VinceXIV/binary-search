#! /c/Users/HP/AppData/Local/Programs/Python/Python310/python
import re
import sys
from pathlib import Path


filePath = sys.argv[1]

def getInputWordArray(filePath):
    # Get one long string of all words in the file with all values lowercased
    theString = Path(filePath).read_text().replace("\n", " ").lower()

    # Perform some sanity checks. Here, I did the following;
    # 1. Remove all non-alphanumeric characters.
    # 2. Accept words such as "ice-cream" (words that have a hyphen) between two words
    # Note that we are not accepting words with a hyphen at the start or end
    sanitizedWordList = re.sub(r'[^(a-zA-Z0-9)-?(a-zA-Z0-9)$]', ' ', theString)

    return sanitizedWordList.split()


# IMPLEMENTATION GRAMMAR CHECK USING BINARY SEARCH

myDictionaryList = Path('./dictionary.txt').read_text().lower().split("\n")
print(myDictionaryList)

def wordExists(testWord, dictionaryWordList=myDictionaryList):
    rangeToCheck = {"start": 0, "end": len(dictionaryWordList)-1}   

    while rangeToCheck["start"] <= rangeToCheck["end"]:
        midPoint = int((rangeToCheck["end"] + rangeToCheck["start"])/2)
        midWord = dictionaryWordList[midPoint]

        if midWord == testWord:
            return True
        elif midWord < testWord:
            rangeToCheck["start"] = midPoint + 1

        elif midWord > testWord:
            rangeToCheck["end"] = midPoint -1
    
    return False


def CheckGrammarUsingBinarySearch(testWordList, dictionaryWordList=myDictionaryList):
    print("The following words were not found in the dictionary;")

    for word in testWordList:
        if not wordExists(word):
            print(word)
        else:
            continue


CheckGrammarUsingBinarySearch(getInputWordArray(filePath))



# # IMPLEMENTATION USING A PYTHON SET

# myDictionarySet = set(Path('./dictionary.txt').read_text().split("\n"))

# def checkGrammar(testWordList, dictionaryWordSet=myDictionarySet):
#     print("The following words were not found in the dictionary;")

#     for word in testWordList:
#         if word not in dictionaryWordSet:
#             print("-", word)

# def removeWeirdCharacters(wordString):
#     return wordString.replace("\n", " ") #for now I'm only dealing with new line


# checkGrammar(myDictionarySet, getInputWordArray(fn))