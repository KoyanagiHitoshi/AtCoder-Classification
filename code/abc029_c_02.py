N=int(input())
def dfs(string):
    if len(string)==N:
        print(string)
        return
    for char in "abc":
        dfs(string+char)
dfs("")