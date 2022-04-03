N=int(input())
div=1
index=0
while div<=N:
    index+=1
    div=2**index
print(div//2)