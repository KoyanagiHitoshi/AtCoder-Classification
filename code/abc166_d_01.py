X=int(input())
MAX,MIN=0,0
diff=0
while diff<=10**9:
    MAX+=1
    diff=MAX**5-(MAX-1)**5
diff=0
while diff<=10**9:
    MIN-=1
    diff=MIN**5-(MIN-1)**5
for A in range(MIN,MAX):
    for B in range(MIN,MAX):
        if A**5-B**5==X:
            print(A,B)
            exit()