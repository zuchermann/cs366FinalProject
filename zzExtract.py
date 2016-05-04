import nltk
import json
from nltk.book import text1
from nltk.book import text2

punctuation = "!?...,;:-(){}[]'\"\\&*_$"
letters = "abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
vowels = "aeiou"

def semanticRichness(text):
    words = set()
    count = []
    # Create a list of words
    for word in text:
        words.add(word)
    return len(words)/(len(text))

def uniqueWords(text):
    unique = []
    num_unique = 200
    for i in range(num_unique):
        unique.append(list())
    words = {}
    for word in text:
        if word in words.keys():
            words[word] = words[word] + 1
        else:
            words[word] = 1
    for key in words.keys():
        i = 0
        while i < num_unique:
            if words[key] == i:
                unique[i].append(len(key))
            i = i + 1
    lengths = []
    for ls in unique:
        val = 0
        if len(ls) != 0:
            acc = 0
            for num in ls:
                acc = acc + num
            val = acc/len(ls)
        lengths.append(val)
    return lengths


def avgSentenceLength(text):
    prevPunc = 0
    numSent = 0
    acc = 0
    for i in range(len(text)):
        if text[i] in ".?!":
            numSent += 1
            #if(i - prevPunc > 30):
                #print(text[prevPunc:i + 1])
            prevPunc = i
        if text[i][0] in punctuation or text[i][0] in numbers:
            acc += 1
            if(text[i] == "-"):
                acc +=1
    return((len(text) - acc)/numSent)

def simpleCompexity(word):
    i = 0
    for lett in word:
        if lett in vowels:
            i += 1
    return 100 * (i/len(word))

def isWord(word):
    if word[0] in punctuation:
        return False
    if word[len(word)-1] in numbers:
       return False
    return True

def singlesCompexity(text):
    words = {}
    singles = {}
    for i in range(len(text)):
        if text[i] in words.keys():
            words[text[i]] = -1
        else:
            words[text[i]] = i
    for key in words:
        if words[key] > 0:
            data = {'location': i/len(text),'complexity': simpleCompexity(key)}
            singles[key] = data
    return singles

def mostUsedCompexity(text):
    words = {}
    for i in range(len(text)):
        if isWord(text[i]):
            if text[i] in words.keys():
                words[text[i]] += 1
            else:
                words[text[i]] = 1
    mostUsed = {}
    #sorts the keys of words by thier values
    sort = sorted(words, key=words.__getitem__)
    sort = sort[len(sort)-51:]
    for key in words:
        if key in sort:
            mostUsed[key] = simpleCompexity(key)
    return mostUsed 


def toJSON(text):
    data = {}
    #use moby dick for testing
    data['semanticRichness'] = semanticRichness(text)
    data['uniqueWords'] = uniqueWords(text)
    data['averageSentenceLength'] = avgSentenceLength(text)
    data['singlesCompexity'] = singlesCompexity(text)
    data['mostUsedComplexity'] = mostUsedComplexity(text)
    with open("features.json", "wt") as out_file:
        json.dump(data, out_file)
