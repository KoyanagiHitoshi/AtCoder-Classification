ABC=sorted(map(int,input().split()))
total=2*ABC[2]-ABC[1]-ABC[0]
print((total+3)//2 if total%2 else total//2)