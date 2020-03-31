N=int(input())
dictionary={}
count=0
for i in range(N):
    s=tuple(sorted(input()))
    if s in dictionary:
        dictionary[s]+=1
        count+=dictionary[s]
    else:
        dictionary[s]=0
print(count)