N=int(input())
S=input()
count=1
for i in range(97,123):
    count*=S.count(chr(i))+1
print((count-1)%(10**9+7))