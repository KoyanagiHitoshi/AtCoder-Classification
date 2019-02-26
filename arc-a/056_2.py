#!/usr/bin/env python
# -*- conding: utf-8 -*-

A,B,K,L=map(int,input().split())
print(min(A*K,(K//L*B+min((K%L)*A,B))))
