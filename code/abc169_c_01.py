from decimal import Decimal,getcontext
A,B=input().split()
getcontext().rounding
print(int(Decimal(A)*Decimal(B)))