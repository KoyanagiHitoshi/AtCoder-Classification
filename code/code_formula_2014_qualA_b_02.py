a,b=map(int,input().split())
p=input().split()
q=input().split()
pin="7 8 9 0\n 4 5 6\n  2 3\n   1"
for i in p:
    pin=pin.replace(i,".")
for i in q:
    pin=pin.replace(i,"o")
for i in range(10):
    pin=pin.replace(str(i),"x")
print(pin)