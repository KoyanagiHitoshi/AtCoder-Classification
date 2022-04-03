N=int(input())
divisors=[]
for num in range(1,int(N**.5)+1):
    if N%num==0:
        divisors.append(num)
        if num!=N//num:
            divisors.append(N//num)
for d in sorted(divisors):
    print(d)