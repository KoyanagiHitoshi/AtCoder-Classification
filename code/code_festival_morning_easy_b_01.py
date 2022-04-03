n=int(input())
mod=n%40
print(1 if mod==0 else mod if mod<21 else 41-mod)