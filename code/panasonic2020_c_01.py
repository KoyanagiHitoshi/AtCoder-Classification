from decimal import Decimal
a,b,c=map(int,input().split())
print("Yes" if Decimal(a).sqrt()+Decimal(b).sqrt()<Decimal(c).sqrt() else "No")