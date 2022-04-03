N=int(input())
print(sum(1-eval(input().replace(" ","-")) for i in range(N)))