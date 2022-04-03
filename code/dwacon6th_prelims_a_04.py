N=int(input())
playlist={}
time=0
for i in range(N):
    s,t=input().split()
    time+=int(t)
    playlist[s]=time
X=input()
print(time-playlist[X])