N = int(input())
alphabet = []
total = 0
for i in range(N):
    a, n = input().split()
    alphabet.append(a)
    total += int(n)
print(alphabet)
print(total)
