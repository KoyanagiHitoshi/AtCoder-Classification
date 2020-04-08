def dfs(x,y,z):
    if x<y or y<z or z<0:return 0
    if x<2 or y<1:return 1
    return dfs(x-1,y,z)+dfs(x,y-1,z)+dfs(x,y,z-1)
a1,a2,a3=map(int,input().split())
print(dfs(a1,a2,a3))