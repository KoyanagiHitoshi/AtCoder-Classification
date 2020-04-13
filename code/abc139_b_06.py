A, B = map(int, input().split())
count, outlet = 0, 1
while outlet < B:
    outlet -= 1
    outlet += A
    count += 1
print(count)