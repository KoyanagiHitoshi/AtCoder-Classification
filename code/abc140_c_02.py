N=int(input())
B=list(map(int,input().split()))
B+=[max(B)]
print(sum(min(B[i-1],B[i]) for i in range(N)))