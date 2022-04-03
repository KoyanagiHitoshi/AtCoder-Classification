N=int(input())
s=[input() for i in range(N)]
for x in zip(*s):
    print("".join(x)[::-1])