h,w=map(int,input().split())
a=[[j for j in input()] for i in range(h)]
b=[]
for x in a:
    if "#" in x:b.append(x)
c=[]
for y in zip(*b):
    if "#" in y:c.append(y)
for a in zip(*c):print("".join(a))