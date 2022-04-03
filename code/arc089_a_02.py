N = int(input())
count = 0
dt, dx, dy = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-dx)+abs(y-dy) <= t-dt and t % 2 == (x+y) % 2:
        count += 1
    dt, dx, dy = t, x, y
print("Yes" if count == N else "No")