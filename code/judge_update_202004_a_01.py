S, L, R = map(int, input().split())
print(L if S <= L else R if R <= S else S)
