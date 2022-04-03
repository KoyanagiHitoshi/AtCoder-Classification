A,B=input().split()
for a,b in zip(A[::-1],B[::-1]):
	if int(a)+int(b)>=10:
		print("Hard")
		break
	else:
		continue
else:
	print("Easy")