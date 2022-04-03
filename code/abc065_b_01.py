N=int(input())
a=[int(input()) for i in range(N)]
count=1
button=a[0]
while button!=2 and count<N:
    count+=1
    button=a[button-1]
print(count if count<N else -1)
