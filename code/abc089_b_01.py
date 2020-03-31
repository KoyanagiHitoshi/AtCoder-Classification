input()
print("Three" if len(set(map(str,input().split())))==3 else "Four")