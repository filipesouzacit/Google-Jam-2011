#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:41:56 2021

@author: filipe
"""
def search(v,i=0,inic=['P'],c=0):
    global bestCost,bestSol
    if i < len(v):
        for v_ in v[i]:
            search(v,i+1, inic + [v_],c+cost[inic[-1]+v_])
    else:
        if c < bestCost:
            bestCost = c
            bestSol = inic[1:]
t = int(input()) 
for i_ in range(1, t + 1):
    line = input().split(" ")
    CJ = int(line[0])
    JC = int(line[1])
    m1  = line[2]
    m1  = 'P'+m1+'P' 
    m = []
    m[:0]=m1
    i=0
    oneS={'CC':'C' if min(0,CJ+JC)==0 else 'J',
            'CJ':'C',
            'PP':'C',
            'JC':'C',
            'JJ':'J' if min(0,CJ+JC)==0 else 'C',
            'JP':'J' if min(0,JC)==0 else 'C',
            'PJ':'J' if min(0,CJ)==0 else 'C',
            'CP':'C' if min(0,CJ)==0 else 'J',
            'PC':'C' if min(0,JC)==0 else 'J'}
    cost = {'CC':0,
            'CJ':CJ,
            'JC':JC,
            'JJ':0,
            'JP':0,
            'PJ':0,
            'CP':0,
            'PC':0,
            'PP':0}
    subProblem = []
    while i < len(m):
        if m[i]=='?':
            j= i+1
            while (m[j]=='?'):
                j+=1
            subProblem.append((i,j-1))
            i = j-1
        i +=1
    for i,j in subProblem:
        if i==j:
            m[i]= oneS[m[i-1]+m[i+1]]
        elif(min(CJ,JC)>=0):
            temp= oneS[m[i-1]+m[j+1]]
            for ii in range(i,j+1):
                m[ii]=temp
        else:
            temp= oneS[m[i-1]+m[j+1]]
            m_ =[m[i-1]]+[ '?' for ii in range(i,j+1)] +[m[j+1]]
            bestSol =[m[i-1]]+[ temp for ii in range(i,j+1)] +[m[j+1]]
            bestCost = cost[m_[0]+temp] + cost[temp+m_[-1]]
            v = []
            for i_ in range(len(m_)):
                v.append(['C','J'] if m_[i_]=='?'else [m_[i_]])
            search(v)
            m[i:j+1] = bestSol[1:-1]
    c=0
    for i in range(1,len(m)-2):
       c+=cost[m[i]+m[i+1]] 
    print("Case #{}: {}".format(i_, c))