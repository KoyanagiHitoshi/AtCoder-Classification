H=int(input())
def attack(x):
    if x<=1:
        return 1
    return 2*attack(x//2)+1
print(attack(H))