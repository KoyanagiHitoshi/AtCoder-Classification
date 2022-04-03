import math
A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())
if V!=W:
    if V>W and math.ceil(abs(B-A)/(V-W))<=T:
        print("YES")
        exit()
print("NO")