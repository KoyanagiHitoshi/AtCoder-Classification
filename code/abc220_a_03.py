A,B,C=map(int,input().split())
mod=B-B%C
print(mod if A<=mod else -1)