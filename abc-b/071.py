#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=sorted(list(set(input())))
if len(s) == 26:
    print("None")
else:
    for i in range(97,123):
        if chr(i) not in s:
            print(chr(i))
            exit()
