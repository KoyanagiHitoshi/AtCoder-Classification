H,W=map(int,input().split())
print("Possible" if H+W-1==sum(input().count("#") for h in range(H)) else "Impossible")