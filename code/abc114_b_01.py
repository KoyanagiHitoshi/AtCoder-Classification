x=input()
d=999
a=0
for i in range(len(x)-2):
    a=int(x[i:i+3])
    d=min(d,abs(a-753))
print(d)