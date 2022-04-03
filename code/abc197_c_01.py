N=int(input())
A=list(map(int,input().split()))
ans=2**30
if len(A)==1:
    print(A[0])
else:
    for bit in range(2**(N-1)):
        bit_or=A[0]
        bit_xor=0
        for i in range(1,N):
            if (bit>>(i-1)&1):
                bit_xor^=bit_or
                bit_or=0
                bit_or|=A[i]
            else:
                bit_or|=A[i]
        bit_xor^=bit_or
        ans=min(ans,bit_xor)
    print(ans)