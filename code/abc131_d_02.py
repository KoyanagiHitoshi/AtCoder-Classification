N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x:x[1])
time=0
for A,B in AB:
    time+=A
    if time>B:
        print("No")
        break
else:
    print("Yes")