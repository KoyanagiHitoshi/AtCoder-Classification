N=int(input())
a=sorted(map(int,input().split()))[::-1]
print(sum(a[1:2*N+1:2]))