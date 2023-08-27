from decimal import Decimal, ROUND_HALF_UP
x = 123.456
print(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
print(Decimal(str(x)).quantize(Decimal("1.0"), rounding=ROUND_HALF_UP))
print(Decimal(str(x)).quantize(Decimal("1.00"), rounding=ROUND_HALF_UP))
