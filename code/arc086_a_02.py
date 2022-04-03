from collections import Counter
N,K=map(int,input().split())
A=Counter(input().split())
ball=0
numbers,counts=zip(*A.most_common())
for num,(key,count) in enumerate(zip(numbers,counts)):
    if num>K-1:
        ball+=count
print(ball)