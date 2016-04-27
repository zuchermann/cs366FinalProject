import nltk
import json
from nltk.book import text1

def semanticRichness(text):
    words = set()
    count = []
    for word in text:
        words.add(word)
    # This is the dictionary data type
    wordCount = dict((x,0) for x in words)
    for word in text:
        wordCount[word] += 1
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
               # count = 999
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

def toJSON():
    text = text1
    data = {}
    #use moby dick for testing
    data['semanticRichness'] = semanticRichness(text)
    data['uniqueWords'] = uniqueWords(text)
    with open("features.json", "wt") as out_file:
        json.dump(data, out_file)
