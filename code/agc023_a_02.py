N=int(input())
A=list(map(int,input().split()))
cumulative_sum=0
count=0
counter={0:1}
for a in A:
    cumulative_sum+=a
    if cumulative_sum not in counter:
        counter[cumulative_sum]=0
    count+=counter[cumulative_sum]
    counter[cumulative_sum]+=1
print(count)