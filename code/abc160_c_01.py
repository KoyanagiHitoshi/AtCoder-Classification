K,N=map(int,input().split())
A=list(map(int,input().split()))
A+=[A[0]+K]
print(K-max(A[i+1]-A[i] for i in range(N)))