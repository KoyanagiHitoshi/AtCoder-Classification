a,b,c=100,100,200
for i in range(17):
    prize=a+b+c
    a,b,c=b,c,prize
print(prize)