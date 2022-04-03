N=int(input())
S=set(input() for i in range(N))
for s in S:
    if "!"+s in S:
        print(s)
        break
else:
    print("satisfiable")