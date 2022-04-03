editor=[]
s=input()
for key in s:
    if key=="B":
        try:
            editor.pop()
        except:
            pass
    else:
        editor.append(key)
print("".join(editor))