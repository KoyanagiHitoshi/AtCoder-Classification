n=int(input())
s=[]
p=[]
for i in range(n):
    S,P=input().split()
    s.append([S,int(P),int(i)+1])
    p.append(int(P))
A=s[::]
A.sort(key=lambda A:(A[1],A[0]),reverse=True)
A.sort(key=lambda A:(A[0]))
for i in range(n):
    print(A[i][2])