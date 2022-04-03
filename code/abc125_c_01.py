import math
N=int(input())
A=list(map(int,input().split()))
right,left=[0],[0]
for i in range(N-1):
    right+=[math.gcd(right[i],A[i])]
    left+=[math.gcd(left[i],A[-i-1])]
print(max(math.gcd(right[i],left[-i-1]) for i in range(N)))