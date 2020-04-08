N, K = map(int, input().split())
H = list(map(int, input().split()))
count = 0
for h in H:
    if h >= K:
        count += 1
print(count)