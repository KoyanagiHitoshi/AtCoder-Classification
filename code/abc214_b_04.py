S, T = map(int, input().split())
ans = 0
for a in range(S+1):
    for b in range(S-a+1):
        for c in range(S-a-b+1):
            if a*b*c <= T:
                ans += 1
print(ans)