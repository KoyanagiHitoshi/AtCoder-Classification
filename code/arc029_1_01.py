N=int(input())
T=[int(input()) for i in range(N)]
grill1=grill2=0
for t in sorted(T)[::-1]:
    if grill1<grill2:
       grill1+=t
    else:
       grill2+=t
print(max(grill1,grill2))