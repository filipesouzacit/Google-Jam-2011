#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:48:20 2021

@author: filipe
"""

import sys

#N,Q = 10,30

def solve():
    global N,Q,q_
    s = []
    i = list(map(str,range(1,N+1)))
    qu = i[:3]
    i = i[3:]
    print(' '.join(qu))
    q_ +=1 
    if q_ >=Q:
        quit()
    sys.stdout.flush()
    an = input()
    qu.remove(an)
    s = [qu[0]] + [an] +  [qu[1]]
    while len(i):
        e = i.pop()
        lenS = len(s)
        js = list(range(lenS))
        while len(js) > 0:
            ids = int(len(js)/2)
            ids -=  1 if ((ids+1)==len(js)) and (ids > 0) else 0
            j = js[ids]
            if (j+1) == lenS:
                if ids==0:
                    js = [j-1]+js
                    j -=1
#                j-= 2 if (j-2)>=0 else 1
            print(' '.join(s[j:j+2]+[e]))
            q_ +=1 
            if q_ >=Q:
                quit()
            sys.stdout.flush()
            an = input()
            if an==e:
                s = s[:j+1] + [e] + s[j+1:]
                js = []
            elif(s[j+1]==an):
                js = js[js.index(j+1)+1:]
                if len(js)==0:
                    s = s[:j+2] + [e] + s[j+2:]
            else:
                js = js[:js.index(j)]
                if len(js)==0:
                    s = s[:j] + [e] + s[j:]
                        
    print(' '.join(s))
    sys.stdout.flush()
    an = input()
    if an == "-1":
      quit()
    
T_,N,Q = map(int, input().split())
q_ = 0
for _ in range(T_):
    solve()
    if q_ >=Q:
        quit()