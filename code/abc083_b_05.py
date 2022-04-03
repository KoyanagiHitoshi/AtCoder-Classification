N,A,B=map(int,input().split())
total=0
for num in range(N+1):
    digit=0
    for i in str(num):
        digit+=int(i)
    if A<=digit<=B:
        total+=num
print(total)