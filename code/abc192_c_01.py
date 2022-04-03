N,K=map(int,input().split())
a=N
for i in range(K):
    a=int("".join(sorted(map(str,str(a)))[::-1]))-int("".join(sorted(map(str,str(a)))))
print(a)