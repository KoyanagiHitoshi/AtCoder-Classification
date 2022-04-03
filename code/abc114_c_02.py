N=int(input())
def dfs(string):
    if int(string)>N:
        return 0
    count=1 if all(string.count(char)>0 for char in "753") else 0
    for char in "753":
        count+=dfs(string+char)
    return count
print(dfs("0"))