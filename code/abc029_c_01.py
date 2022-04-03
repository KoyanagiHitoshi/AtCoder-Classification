from itertools import product
N=int(input())
[print("".join(i)) for i in product("abc",repeat=N)]