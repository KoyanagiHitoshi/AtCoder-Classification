s=list(input()[::-1])
for i in range(len(s)-1):
    if s[i]=="A" and s[i+1]=="W":
        s[i],s[i+1]="C","A"
print("".join(s[::-1]))