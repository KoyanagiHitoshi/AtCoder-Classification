n,k=map(int,input().split())
print(sum(sorted(map(int,input().split()))[-k:]))