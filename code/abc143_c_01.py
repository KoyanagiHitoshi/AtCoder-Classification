N=int(input())
S=input()
count=1
for n in range(1,N):
    if S[n]!=S[n-1]:
        count+=1
print(count)