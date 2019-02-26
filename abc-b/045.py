#!/usr/bin/env python
# -*- conding: utf-8 -*-

A=list(input())
B=list(input())
C=list(input())
f=A[0]
while any([len(A)!=0,len(B)!=0,len(C)!=0]):
    if f=="a":f=A.pop(0)
    elif f=="b":f=B.pop(0)
    elif f=="c":f=C.pop(0)
    print(A)
    print(B)
    print(C)
    print()
if(len(A)==0):print("A")
if(len(B)==0):print("B")
if(len(C)==0):print("C")


