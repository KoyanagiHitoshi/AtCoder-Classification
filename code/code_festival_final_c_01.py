A=int(input())
for i in range(10,10**4+1):
    N=str(i)
    k=0
    for j in range(len(N)):
        k+=int(N[-j-1])*(i**j)
    if k==A:
        print(i)
        break
else:
    print(-1)