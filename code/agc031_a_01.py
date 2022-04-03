N=int(input())
S=input()
count=1
for char in set(S):
    count*=S.count(char)+1
print((count-1)%(10**9+7))