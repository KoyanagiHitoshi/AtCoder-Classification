n,k=map(int,input().split())
s=input()
print(s[:k-1].upper()+s[k-1:k].lower()+s[k:].upper())