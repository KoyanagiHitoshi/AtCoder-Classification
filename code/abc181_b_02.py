N=int(input())
total=0
for i in range(N):
    A,B=map(int,input().split())
    total+=B*(B+1)//2-A*(A-1)//2
print(total)