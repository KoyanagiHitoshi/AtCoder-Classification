#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c,d=map(int,input().split())
print("TAKAHASHI" if b/a>d/c else "AOKI" if b/a<d/c else "DRAW")
