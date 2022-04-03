N=int(input())
ST=[]
for i in range(N):
    st=input()
    ST.append(st)
print("Yes" if len(set(ST))!=N else "No")