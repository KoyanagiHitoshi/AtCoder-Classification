n=int(input())
l=[int(_) for _ in input().split()]
print(-(-sum(l)//(n-l.count(0))))