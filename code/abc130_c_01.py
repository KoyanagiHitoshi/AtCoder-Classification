W,H,x,y=map(int,input().split())
print(W*H/2,1) if W==2*x and H==2*y else print(W*H/2,0)