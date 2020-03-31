l=sorted(map(int,input().split()))
print("Yes" if sum(l[:2])==l[2] else "No")