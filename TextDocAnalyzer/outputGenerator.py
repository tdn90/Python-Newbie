from dataProcessor import *

def getResult(wordDict):
    words = list(wordDict.keys())
    words.sort()
    file = open("output.txt", 'w')
    numWordsRead = 0
    for word in words:
        file.write('\t{0:>5}\t{1:<}\n'.format(wordDict.get(word), word))
        numWordsRead += wordDict.get(word)
    file.write("-----------------------\n")
    file.write('\t{0:>5}\t{1:<}\n'.format(len(words), 'Number of distinct words'))
    file.write('\t{0:>5}\t{1:<}\n'.format(numWordsRead, 'Total words read'))
    file.close()
