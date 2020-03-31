l=sorted(map(int,input().split()))
a=2*l[2]-l[1]-l[0]
print((a+3)//2 if a%2 else a//2)