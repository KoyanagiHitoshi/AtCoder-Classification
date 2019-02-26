#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = int(input())
prime = 0
for i in range(105, N+1, 2):
    count = 0
    for j in range(1, i+1):
        if(i%j == 0):
            count += 1
    if(count == 8):
        prime += 1
print(prime)
