#!/usr/bin/env python
# -*- conding: utf-8 -*-

[(a,b,c),(d,e,f),(g,h,i)]=[map(int,input().split()) for _ in range(3)]
print("Yes" if a-b==d-e==g-h and b-c==e-f==h-i else "No")
