N=int(input())
s=[input() for i in range(N)]
for x in zip(*reversed(s)):
    print("".join(x))