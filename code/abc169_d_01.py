def factorization(N):
    factoring={}
    num=N
    for i in range(2,int(N**.5)+1):
        if num%i==0:
            count=0
            while num%i==0:
                count+=1
                num//=i
            factoring[i]=count
    if num!=1:
        factoring[num]=1
    return factoring

N=int(input())
prime=factorization(N)
count=0
for num in prime:
    e=1
    while prime[num]>=e:
        count+=1
        prime[num]-=e
        e+=1
print(count)