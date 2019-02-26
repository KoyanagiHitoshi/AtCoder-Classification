#!/usr/bin/env python
# -*- conding: utf-8 -*-

print(all(s==t or s+t in"@a@t@c@o@d@e@r@"for s,t in zip(input(),input()))and"You can win"or"You will lose")
