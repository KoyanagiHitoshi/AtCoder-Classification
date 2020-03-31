L,R=map(int,input().split())
left=L%2019
right=R%2019
print(0 if R-L>=2019 else min([i*j%2019 for i in range(left,right+1) for j in range(i+1,right+1)]))