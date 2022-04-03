N=int(input())
count=0
count+=max(0,N-int(str(9)*3))
count+=max(0,N-int(str(9)*6))
count+=max(0,N-int(str(9)*9))
count+=max(0,N-int(str(9)*12))
count+=max(0,N-int(str(9)*15))
print(count)