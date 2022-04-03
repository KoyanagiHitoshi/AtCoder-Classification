N=int(input())
total=0
maximum=100
for i in range(N):
    p=int(input())
    total+=p
    maximum=max(maximum,p)
print(total-maximum//2)