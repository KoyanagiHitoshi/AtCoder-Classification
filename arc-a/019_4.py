#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=input()
print(S.maketrans("ODIZSB","001258"))
print(S.translate(str.maketrans("ODIZSB","001258")))
