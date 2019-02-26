#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = input()
print("Yes" if int(N) % sum(int(_) for _ in N) == 0 else "No") 
