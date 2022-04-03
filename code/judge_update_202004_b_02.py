N=int(input())
red=[]
blue=[]
for i in range(N):
    X,C=input().split()
    X=int(X)
    if C=="R":
        red.append(X)
    else:
        blue.append(X)
for r in sorted(red):
    print(r)
for b in sorted(blue):
    print(b)