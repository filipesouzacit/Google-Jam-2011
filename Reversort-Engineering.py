#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:46:23 2021

@author: filipe
"""
t = int(input()) 
for i_ in range(1, t + 1):
    n , c = [int(s) for s in input().split(" ")]
    if (n > c+1) or (sum(range(2,n+1))<c):
         a = 'IMPOSSIBLE'
    else:
        cr = n-1
        dif = 0
        for i in range(n-1):
            cr += n-i-1
            if cr>c:
                dif = cr-c
                break
        j = 0
        b = 0
        e = n
        flg = True
        l = list(range(1,n+1))
        for j in range(i):  
            l[b:e]=list(reversed(l[b:e]))
            if flg:
                e-=1
            else:
                b+=1
            flg = not(flg)
        if flg:
            e-=dif
        else:
            b+=dif
        l[b:e]=list(reversed(l[b:e]))
        a = ' '.join(map(str,l))
    print("Case #{}: {}".format(i_, a))