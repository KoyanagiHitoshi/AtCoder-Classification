#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
print(Counter([input() for i in range(int(input()))]).most_common()[0][0])
