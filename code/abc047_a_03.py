abc=sorted(map(int,input().split()))
print("Yes" if sum(abc[:2])==abc[2] else "No")