A,B=map(int,input().split())
print(len([num for num in map(str,range(A,B+1)) if num==num[::-1]]))