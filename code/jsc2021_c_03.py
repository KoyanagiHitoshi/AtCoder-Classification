A,B=map(int,input().split())
for c in range(B,0,-1):
    if B//c-(A+c-1)//c>=1:
        exit(print(c))