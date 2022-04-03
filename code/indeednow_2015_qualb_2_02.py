s=input()
t=input()
count=0
if len(s)==len(t):
    t*=2
    for i in range(len(s)):
        if s!=t[i:len(s)+i]:
            count+=1
        else:
            print(count)
            break
    else:
        print(-1)
else:
    print(-1)