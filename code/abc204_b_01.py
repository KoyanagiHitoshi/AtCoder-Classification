N=int(input())
A=list(map(int,input().split()))
total=0
for a in A:
    total+=max(0,a-10)
print(total)