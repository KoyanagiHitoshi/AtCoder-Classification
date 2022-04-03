N=int(input())
L=sorted(map(int,input().split()))
count=0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if L[k]+L[j]>L[i] and L[k]!=L[j]!=L[i]:
                count+=1
print(count)