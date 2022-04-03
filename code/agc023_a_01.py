from collections import Counter
N=int(input())
A=list(map(int,input().split()))
cumulative_sum=0
count=0
counter=Counter([0])
for a in A:
    cumulative_sum+=a
    count+=counter[cumulative_sum]
    counter[cumulative_sum]+=1
print(count)