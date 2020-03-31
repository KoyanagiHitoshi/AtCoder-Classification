N=int(input())
H=list(map(int,input().split()))
base=0
for h in H:
    if base>h:
        print("No")
        break
    base=max(base,h-1)
else:
    print("Yes")