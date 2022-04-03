a,b=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
pin=["x"]*10
for i in p:
    pin[i-1]="."
for i in q:
    pin[i-1]="o"
print(" ".join(pin[6:10]))
print(" "+" ".join(pin[3:6]))
print("  "+" ".join(pin[1:3]))
print("   "+pin[0])