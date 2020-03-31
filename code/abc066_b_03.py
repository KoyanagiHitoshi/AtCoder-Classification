s=list(input())
while len(s)!=0:
    s.pop()
    if len(s)%2==0 and s[:len(s)//2]==s[len(s)//2:]:
        print(len(s))
        exit()