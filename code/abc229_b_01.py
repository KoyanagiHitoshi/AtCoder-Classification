A,B=input().split()
A,B=A[::-1],B[::-1]
for i in range(min(len(A),len(B))):
	if int(A[i])+int(B[i])>=10:
		print("Hard")
		break
	else:
		continue
else:
	print("Easy")