S=list(input().split())
program=[]
for s in S:
    if s=="Left":
        program.append("<")
    elif s=="Right":
        program.append(">")
    else:
        program.append("A")
print(" ".join(program))