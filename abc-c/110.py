#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
s=Counter(list(input()))
t=Counter(list(input()))
s,t=list(s.values()),list(t.values())
print("Yes" if sorted(s)==sorted(t) else "No")
