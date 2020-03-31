n,k=map(int,input().split())
l=sorted([int(_) for _ in input().split()])
print(sum(l[-k:]))