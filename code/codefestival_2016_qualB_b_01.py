N,A,B=map(int,input().split())
S=input()
a=b=0
for s in S:
    if s=="a" and a+b<A+B:
        a+=1
        print("Yes")
    elif s=="b" and a+b<A+B and b<B:
        b+=1
        print("Yes")
    else:
        print("No")