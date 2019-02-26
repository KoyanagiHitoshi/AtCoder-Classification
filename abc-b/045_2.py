#!/usr/bin/env python
# -*- conding: utf-8 -*-

S={c:list(input()) for c in "abc"}
s="a"
while S[s]:s=S[s].pop(0)
print(s.upper())
