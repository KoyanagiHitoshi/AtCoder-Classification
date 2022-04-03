A,B=map(int,input().split())
print(sum(num==num[::-1] for num in map(str,range(A,B+1))))