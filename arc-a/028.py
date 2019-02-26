#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,A,B=map(int,input().split())
print("Ant" if 0<N%(A+B)<=A else "Bug")
