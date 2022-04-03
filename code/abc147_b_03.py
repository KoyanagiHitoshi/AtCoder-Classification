S=input()
print(sum(x!=y for x,y in zip(S,S[::-1]))//2)