h,w=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
grid=[list(input()) for x in range(h)]
grid[sy-1][sx-1]=0
loc=[[sy-1,sx-1]]
for k in range(1,h*w):
    next_loc=[]
    for y,x in loc:
        for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
            if grid[y+i][x+j]=='.':
                grid[y+i][x+j]=k
                next_loc.append([y+i,x+j])
    loc=next_loc
    if [gy-1,gx-1] in loc:
        break
print(k)