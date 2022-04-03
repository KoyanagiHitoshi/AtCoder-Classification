X=int(input())
year=0
deposit=100
while deposit<X:
    deposit=deposit+int(deposit*0.01)
    year+=1
print(year)