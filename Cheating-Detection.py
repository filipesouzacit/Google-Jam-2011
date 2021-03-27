#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:50:29 2021

@author: filipe
"""
import numpy as np
t = int(input())
p = int(input()) 
for i_ in range(1, t + 1):
    data = []
    for i in range(100):
        temp= []
        temp[:0] = input()
        data.append(list(map(int,temp)))
        assert (len(temp)==10000)
    data  = np.array(data)
    skill = np.sum(data,axis=1)/10000
    dif   = np.sum(data,axis=0)/100
    data1 = skill.reshape((100,1))+dif.reshape((1,10000))
    data1 = 1/(1 + np.exp(-data1))
    data2 = data * np.log(data1)+(1-data)*np.log(1-data1)
    data2 = np.abs(data2)
    dd = list(np.argmax(data2,axis=0)) + list(np.argmin(data2,axis=0)) 
    c = max(set(dd), key=dd.count)+1 
    print("Case #{}: {}".format(i_, c))