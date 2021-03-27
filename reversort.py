#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:38:47 2021

@author: filipe
"""

t = int(input()) 
for i in range(1, t + 1):
  n = int(input())
  l = [int(s) for s in input().split(" ")]
  c=0 
  for i_ in range(n-1):
      j = l.index(min(l[i_:]))
      c+=1
      if j > i_:
          lt = l[i_:j+1]
          lt.reverse()
          l[i_:j+1] = lt
          c+=j-i_
  print("Case #{}: {}".format(i, c))