A,B=map(int,input().split())
print(sum(i==i[::-1] for i in map(str,range(A,B+1))))