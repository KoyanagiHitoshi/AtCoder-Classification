N=int(input())
div=1
for i in range(7):
    if 2**i<=N:
        div=2**i
print(div)