A,B,X=map(int,input().split())
minimum=0
maximum=10**9+1
while maximum-minimum>1:
    medium=(maximum+minimum)//2
    if A*medium+B*len(str(medium))>X:
        maximum=medium
    else:
        minimum=medium
print(minimum)