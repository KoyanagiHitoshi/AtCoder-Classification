S={char:list(input()) for char in "abc"}
turn="a"
while S[turn]:
    turn=S[turn].pop(0)
print(turn.upper())