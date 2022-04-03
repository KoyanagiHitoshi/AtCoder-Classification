N=int(input())
count=0
for a in range(1,N):
    count+=(N-1)//a
print(count)