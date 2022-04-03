N=sorted(input())[::-1]
x=N[0::2]
y=N[1::2]
for i in range(min(len(x),len(y))):
	if x[i]!=y[i]:
		x[i],y[i]=y[i],x[i]
		break
print(int("".join(x))*int("".join(y)))