N=int(input())
A=list(map(int,input().split()))
S=0
for a in A:
    S=2*S+a
print(S)