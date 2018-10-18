import sys
from outputGenerator import *

words = []
for arg in sys.argv[1:]:
    words = getWordsFromFile(arg, words)
cleanWords = cleanData(words)
wordDict = count(cleanWords)
getResult(wordDict)

