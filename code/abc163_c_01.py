N=int(input())
A=list(map(int,input().split()))
bosses=[0]*N
for a in A:
    bosses[a-1]+=1
for boss in bosses:
    print(boss)