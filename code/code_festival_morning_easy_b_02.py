n=int(input())
mod=n%40
print(mod if 0<mod<21 else (41-mod)%40)