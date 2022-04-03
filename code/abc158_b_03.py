N,A,B=map(int,input().split())
div,mod=divmod(N,A+B)
print(div*A+min(mod,A))