#!/usr/bin/env python
# -*- conding: utf-8 -*-

print(sum(map(max,zip(*[list(map(int,input().split())) for i in range(2)]))))

