n=int(input())
print(sum(all(i%j for j in range(2,int(i**.5)+1)) for i in range(2,n)))