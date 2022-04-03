X,A,B=map(int,input().split())
print("dangerous" if X<B-A else "safe" if A<B else "delicious")