N,Y=map(int,input().split())
answer=(-1,-1,-1)
for x in range(N+1):
    for y in range(N-x+1):
        z=N-x-y
        if 0<=z<=2000 and 10000*x+5000*y+1000*z==Y:
            answer=(x,y,z)
            break
    else:
        continue
    break
print(*answer)