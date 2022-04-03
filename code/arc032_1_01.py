n=int(input())
total=sum(num for num in range(n+1))
flag=True
for num in range(2,total):
    if total%num==0:
        flag=False
        break
print("WANWAN" if flag and n!=1 else "BOWWOW")