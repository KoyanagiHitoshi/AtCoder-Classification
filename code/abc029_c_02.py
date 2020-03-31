from itertools import product
[print("".join(i)) for i in product("abc",repeat=int(input()))]