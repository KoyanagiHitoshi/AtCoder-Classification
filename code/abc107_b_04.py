h,w=map(int,input().split())
for a in zip(*[y for y in zip(*[x for x in [[j for j in input()] for i in range(h)] if "#" in x]) if "#" in y]):print("".join(a))