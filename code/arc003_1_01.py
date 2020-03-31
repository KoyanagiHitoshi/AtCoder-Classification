N=int(input())
print(sum(map(int,input().translate(str.maketrans("FDCBA","01234"))))/N)