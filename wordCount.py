#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:00:19 2020

@author: CarlosCardenas
"""    

def countWords(rFile,wFile):
    file=open(rFile,"r+")
    wordcount={}

    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    sortedDict = dict( sorted(wordcount.items(), key=lambda x: x[0].lower()) )
    with open(wFile, 'w') as f:
        for k,v in sortedDict.items():
            print(k, v, file=f)

countWords("speech.txt","output.txt")
    
    
