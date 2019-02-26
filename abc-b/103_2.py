#!/usr/bin/env python
# -*- conding: utf-8 -*-

S = list(input())
T = list(input())
tmp = ""
for i in range(len(T)):
    for j in range(0, len(T)-1):
        if j == 0:
            tmp = T[j]
        if j == (len(T)-1):
            T[j+1] = tmp
        T[j] = T[j+1]
    print(T)
    if S == T:
        print("Yes")
        exit()
print("No")

