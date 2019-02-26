#!/usr/bin/env python
# -*- conding: utf-8 -*-

print(sum(1-eval(input().replace(" ","-")) for _ in range(int(input()))))
