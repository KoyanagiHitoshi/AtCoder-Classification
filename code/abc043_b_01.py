editor=""
s=input()
for key in s:
    if key=="B":
        editor=editor[:-1]
    else:
        editor+=key
print(editor)