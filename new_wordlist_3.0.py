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

"""
将wordlist封装在函数中，用于得出文件中的词频最高/低的num个词和词频
@param:输入：
       path:文件路径
       num:用户可以输入想要前几个/后几个词频
@param:输出：
       wl_sorted_desc：正序列表
       wl_sorted_asc：倒序列表
"""
def wordlist(path,num):
    #corpus_root = 'D:/corpara' #文件路径
    corpus_root = path
    files = PlaintextCorpusReader(corpus_root,'.*\.txt')#批量读文件
    #print(files.fileids())
    ff=files.raw(fileids=files.fileids())
    n=num
    #去掉标点符号
    tokenizer = RegexpTokenizer("[\w']+")
    cps = tokenizer.tokenize(ff)
    
    #print(cps)
    
    cps1 = Text(cps)
    
    fdist1 = FreqDist(cps1)
    wl = fdist1.items()
    wl_sorted_desc = sorted(wl, key=lambda w:w[1], reverse=True)#正序排序
    wl_sorted_asc = sorted(wl, key=lambda w:w[1])#倒序排序
    
    print("---------------------------------------------")
    print("Wordlist of Top ",n)
    print(" word  freq*")
    print(" ----  ----")
    i=0
    for i in range(0,n): #打印list中出现最多的num个值
        print(wl_sorted_desc[i])
        i=i+1
    print(type(wl_sorted_desc))    
    print("                                ")
    print("Wordlist of Last ",n)
    print(" word  freq*")
    print(" ----  ----")
    i=0
    for i in range(0,n): #打印list中出现最少的num个值
        print(wl_sorted_asc[i])
        i=i+1
    return (wl_sorted_desc,wl_sorted_asc)
    
    
if __name__ == '__main__':
    path = 'D:/corpara' #将文件存在这个路径下
    a,b=wordlist(path,15) #得到了顺序和倒序的排名
