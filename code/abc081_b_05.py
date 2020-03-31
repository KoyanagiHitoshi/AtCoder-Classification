input()
n=eval(input().replace(' ','|'))
print(len(bin(n&-n))-3)