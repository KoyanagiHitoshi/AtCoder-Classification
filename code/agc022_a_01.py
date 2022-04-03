S=input()
if len(S)<26:
    for char in range(ord("a"),ord("z")):
        if chr(char) not in S:
            break
    print(S+chr(char))
else:
    stack=list(S[-1])
    for s in S[len(S)-2::-1]:
        if s>stack[-1]:
            stack.append(s)
        else:
            break
    if len(stack)==26:
        print(-1)
    else:
        print(S[:-len(stack)-1]+min(s for s in stack if s>S[-len(stack)-1]))