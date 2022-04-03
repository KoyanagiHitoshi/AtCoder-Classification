A,B=map(int,input().split())
print(len([i for i in map(str,range(A,B+1)) if i==i[::-1]]))