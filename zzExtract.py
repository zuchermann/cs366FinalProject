import nltk
import json
from nltk.book import text1
from nltk.book import text2

punctuation = "!?...,;:-(){}[]'\"\\&*_$"
letters = "abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
vowels = "aeiouAEIOU"

# gives the percentage of differant words used over total number of words
def semanticRichness(text):
    words = set()
    count = []
    # Create a list of words
    for word in text:
        words.add(word)
    return len(words)/(len(text))

# returns an array where each slot i has the
# average length of words used i times
def uniqueWords(text):
    unique = []
    num_unique = 200
    # create 200 lists
    for i in range(num_unique):
        unique.append(list())
    words = {}
    # get each word and the number of times it is used
    for word in text:
        if word in words.keys():
            words[word] = words[word] + 1
        else:
            words[word] = 1
    # put each word that is used less than 200 times
    # in a list with other words used with the same frequency 
    for key in words.keys():
        i = 0
        while i < num_unique:
            if words[key] == i:
                unique[i].append(len(key))
            i = i + 1
    lengths = []
    # get the average length of each list and put those lengths in an array
    for ls in unique:
        val = 0
        if len(ls) != 0:
            acc = 0
            for num in ls:
                acc = acc + num
            val = acc/len(ls)
        lengths.append(val)
    return lengths


# gives the average sentance length
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

# gives the complexity defined as the percentage of vowels
def simpleComplexity(word):
    i = 0
    for lett in word:
        if lett in vowels:
            i += 1
    return 100 * (i/len(word))

# tells if the stirng is a word
def isWord(word):
    if word[0] in punctuation:
        return False
    if word[len(word)-1] in numbers:
       return False
    return True

def getKey(item):
    return item[0]

#gives the location and simple complexity of every word only used once
def singlesComplexity(text):
    words = {}
    singles = []
    for i in range(len(text)):
        if text[i] in words.keys():
            words[text[i]] = -1
        else:
            words[text[i]] = i
    for key in words:
        if words[key] > 0:
            data = (words[key],simpleComplexity(key))
            singles.append(data)
    singles = sorted(singles, key=getKey)
    return singles

#gives the complexity of the 50 most used words
def mostUsedComplexity(text):
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
            mostUsed[key] = simpleComplexity(key)
    return mostUsed

# gives the percentage of the tagged text that is verbs
def percentVerbs(taggedText):
    count = 0
    for (x,y) in taggedText:
        if y == "VB":
            count += 1
    return 100 * (count/len(taggedText))

#extracts features from the text and exports them as a JSON
def toJSON(text):
    data = {}
    taggedText = nltk.pos_tag(text)
    data['length'] = len(text)
    data['semanticRichness'] = semanticRichness(text)
    data['uniqueWords'] = uniqueWords(text)
    data['averageSentenceLength'] = avgSentenceLength(text)
    data['singlesComplexity'] = singlesComplexity(text)
    data['mostUsedComplexity'] = mostUsedComplexity(text)
    data['percentVerbs'] = percentVerbs(taggedText)
    with open("features.json", "wt") as out_file:
        json.dump(data, out_file)
