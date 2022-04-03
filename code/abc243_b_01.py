N=int(input())
A=input().split()
B=input().split()
count=0
for a,b in zip(A,B):
    if a==b:
        count+=1
print(count)
print(len(set(A)&set(B))-count)