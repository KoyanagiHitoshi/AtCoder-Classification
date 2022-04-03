N=int(input())
r=input()
print(sum(map(int,r.translate(str.maketrans("FDCBA","01234"))))/N)