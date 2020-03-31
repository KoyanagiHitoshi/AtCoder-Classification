n=int(input())
coin=[]
for i in range(n):
    a,b=map(int,input().split())
    coin.append([min(a,b),max(a,b)])
print(len(list(map(list,set(map(tuple,coin))))))