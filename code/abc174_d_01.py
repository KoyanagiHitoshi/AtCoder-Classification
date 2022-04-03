N=int(input())
c=input()
count=[0 for _ in range(N)]
red=0
for i in range(N):
    if c[i]=="R":
        red+=1
    count[i]=red
print(red-count[red-1])