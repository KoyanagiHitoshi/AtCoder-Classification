L,R=map(int,input().split())
R=min(R,L+2019)
minimum=2018
for i in range(L,R+1):
    for j in range(i+1,R+1):
        minimum=min(minimum,i*j%2019)
print(minimum)