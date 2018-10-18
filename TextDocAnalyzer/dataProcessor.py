def getWordsFromFile(fileName, words):
    file = open(fileName, "r")
    for line in file:
        words.extend(line.split())
    file.close()
    return words

def cleanWord(word):
    word = word.strip(",./<>?;':\"_-`~!()[]{}\\")
    word = word.lower()
    return word

def cleanData(rawData):
    result = []
    for data in rawData:
        word = cleanWord(data)
        if len(word) > 0:
            result.append(word)
    return result

def count(listOfWords):
    wordDict = {}
    for word in listOfWords:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict



        



