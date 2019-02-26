#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = int(input())
for i in range(111, 1000, 111):
    if(N - i <= 0):
        print(i)
        exit()
