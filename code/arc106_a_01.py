num=1
A=B=0
while num<10**18:
    A+=1
    num*=3
num=1
while num<10**18:
    B+=1
    num*=5
N=int(input())
for a in range(1,A):
    for b in range(1,B):
        if 3**a+5**b==N:
            print(a,b)
            exit()
print(-1)