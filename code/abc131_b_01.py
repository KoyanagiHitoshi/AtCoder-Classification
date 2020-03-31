N,L=map(int,input().split())
left=L
right=left+N-1
if right<=0:eated=right
elif 0<left:eated=left
else:eated=0
print((left+right)*(right-left+1)//2-eated)