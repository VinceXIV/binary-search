#! /c/Users/HP/AppData/Local/Programs/Python/Python310/python
import re
import sys
from pathlib import Path


filePath = sys.argv[1]
myDictionaryList = Path('./dictionary.txt').read_text().lower().split("\n")


def getInputWordList(filePath):
    # Get one long string of all words in the file with all values lowercased
    theString = Path(filePath).read_text().replace("\n", " ").lower()

    # Perform some sanity checks. Here, I did the following;
    # 1. Remove all non-alphanumeric characters.
    # 2. Accept words such as "ice-cream" (words that have a hyphen) between two words
    # Note that we are not accepting words with a hyphen at the start or end
    sanitizedWordList = re.sub(r'[^(a-z0-9)-?(a-z0-9)$]', ' ', theString)

    print("Your input contained the following words: ")
    print(sanitizedWordList.split())
    print("")

    return sanitizedWordList.split(" ")



def wordExists(testWord, dictionaryWordList=myDictionaryList):
    searchRange = {"start": 0, "end": len(dictionaryWordList)-1}   

    while searchRange["start"] <= searchRange["end"]:
        midPoint = int((searchRange["end"] + searchRange["start"])/2)
        midWord = dictionaryWordList[midPoint]

        if midWord == testWord:
            return True
        elif midWord < testWord:
            searchRange["start"] = midPoint + 1

        elif midWord > testWord:
            searchRange["end"] = midPoint -1
    
    return False



def CheckGrammarUsingBinarySearch(testWordList):
    print("The following words were not found in the dictionary;")

    index = 1
    for word in testWordList:
        if not wordExists(word):
            print(index, ". ", word)
            index += 1
        else:
            continue



CheckGrammarUsingBinarySearch(getInputWordList(filePath))