N=int(input())
p=list(map(int,input().split()))
diff=0
for i in range(N):
    if p[i]!=i+1:diff+=1
print("YES" if diff==0 or diff==2 else "NO")