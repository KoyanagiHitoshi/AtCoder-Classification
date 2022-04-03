letters="abcdefghijklmnopqrstuvwxyz"
S=input()
ans=sorted(set(letters)^set(S))
print("None" if len(ans)==0 else ans[0])