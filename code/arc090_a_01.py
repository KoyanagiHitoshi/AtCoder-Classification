N=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
print(max(sum(A1[:i+1])+sum(A2[i:]) for i in range(N)))