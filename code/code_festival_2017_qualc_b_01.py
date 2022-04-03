N=int(input())
A=list(map(int,input().split()))
odd=[a%2 for a in A].count(0)
print(3**N-2**odd)