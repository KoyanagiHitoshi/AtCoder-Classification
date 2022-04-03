N=int(input())
K=int(input())
display=1
for i in range(N):
    display=min(display*2,display+K)
print(display)