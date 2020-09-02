#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:00:19 2020

@author: CarlosCardenas
"""

# FILE_NAME = 'speech.txt'


# file=open(FILE_NAME,"r+")
# wordcount={}

# for word in file.read().split():
#     if word not in wordcount:
#         wordcount[word] = 1
#     else:
#         wordcount[word] += 1
#     with open('output.txt', 'w') as f:
#         for k,v in wordcount.items():
#             print(k, v, file=f)
#    # print (k, v)
    

def countWords(rFile,wFile):
    file=open(rFile,"r+")
    wordcount={}

    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    sorted(wordcount)
    with open(wFile, 'w') as f:
        for k,v in wordcount.items():
            print(k, v, file=f)

countWords("speech.txt","output.txt")
    