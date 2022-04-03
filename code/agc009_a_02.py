N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
count=0
for a,b in AB[::-1]:
    a+=count
    if a%b!=0:
        count+=b-(a%b)
print(count)