#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=input()
for b,a in zip("ODIZSB","001258"):
    S=S.replace(b,a)
print(S)
