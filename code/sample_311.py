x = "abcd"
print(x.encode())
print(bytes(i+1 for i in x.encode()).decode())
