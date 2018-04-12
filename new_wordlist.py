# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:40:38 2018

@author: 许某某
"""

from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
corpus_root = 'D:/corpara'
files = PlaintextCorpusReader(corpus_root,'.*\.txt')
#print(files.fileids())
ff=files.raw(fileids=files.fileids())

#去掉标点符号
tokenizer = RegexpTokenizer("[\w']+")
cps = tokenizer.tokenize(ff)

#print(cps)

cps1 = Text(cps)

fdist1 = FreqDist(cps1)
wl = fdist1.items()
wl_sorted_desc = sorted(wl, key=lambda w:w[1], reverse=True)
wl_sorted_asc = sorted(wl, key=lambda w:w[1])

print("---------------------------------------------")
print("Wordlist of Top 10")
print(" word  freq*")
print(" ----  ----")
i=0
for i in range(0,10): #打印list中出现最多的10个值
    print(wl_sorted_desc[i])
    i=i+1
    
print("                                ")
print("Wordlist of Last 10")
print(" word  freq*")
print(" ----  ----")
i=0
for i in range(0,10): #打印list中出现最少的10个值
    print(wl_sorted_asc[i])
    i=i+1