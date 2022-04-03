N=int(input())
a=list(map(int,input().split()))
diff=0
count=N
for i in range(N-1):
    if a[i]<a[i+1]:
        diff+=1
        count+=diff
    else:
        diff=0
print(count)