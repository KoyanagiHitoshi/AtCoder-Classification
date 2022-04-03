N=int(input())
s=[input() for i in range(N)]
reverse=[word[::-1] for word in s]
reverse.sort()
sakasama=[word[::-1] for word in reverse]
print(*sakasama,sep="\n")