N=int(input())
count=0
if N>=10**3:
    count+=N-int(str(9)*3)
if N>=10**6:
    count+=N-int(str(9)*6)
if N>=10**9:
    count+=N-int(str(9)*9)
if N>=10**12:
    count+=N-int(str(9)*12)
if N>=10**15:
    count+=N-int(str(9)*15)
print(count)