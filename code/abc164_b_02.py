A, B, C, D = map(int, input().split())
print("Yes" if (A+D-1)//D >= (C+B-1)//B else "No")