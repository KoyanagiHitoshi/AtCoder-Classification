n,k=map(int,input().split())
print(sum(sorted([int(_) for _ in input().split()])[-k:]))