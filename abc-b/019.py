#!/usr/bin/env python
# -*- conding: utf-8 -*-

import itertools
s=""
for i,j in itertools.groupby(list(input())):
    s+=i+str(len(list(j)))
print(s)

