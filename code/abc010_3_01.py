a,b,c,d,T,V=map(int,input().split())
N=int(input())
for i in range(N):
    x,y=map(int,input().split())
    if T*V>=((a-x)**2+(b-y)**2)**.5+((c-x)**2+(d-y)**2)**.5:
        print("YES")
        exit()
print("NO")