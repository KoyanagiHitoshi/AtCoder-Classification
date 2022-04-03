W,H=map(int,input().split())
print("16:9" if W*H%144==0 else "4:3")