N=int(input())
def divisors(n):
    div=[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    div.sort()
    return div
for d in divisors(N):
    print(d)