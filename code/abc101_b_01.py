N=input()
print("Yes" if int(N)%sum(map(int,N))==0 else "No")