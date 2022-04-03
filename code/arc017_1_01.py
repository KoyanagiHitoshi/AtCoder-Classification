N=int(input())
print("YES" if all(N%num for num in range(2,int(N**.5)+1)) else "NO")