N=int(input())
A=list(map(int,input().split()))
ave=round(sum(A)/N)
print(sum(abs(a-ave)**2 for a in A))