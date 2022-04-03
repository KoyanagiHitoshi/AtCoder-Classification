N=input()[::-1]
print(sum(map(int,N[1::2])),sum(map(int,N[::2])))