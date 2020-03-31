letters="abcdefghijklmnopqrstuvwxyz"
ans=sorted(set(letters)^set(input()))
print("None" if len(ans)==0 else ans[0])