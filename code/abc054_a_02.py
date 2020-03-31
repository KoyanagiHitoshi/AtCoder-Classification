a,b=map(int,input().split())
a,b=(a+13)%15,(b+13)%15
print("Alice" if a>b else "Bob" if a<b else "Draw")