sx,sy,tx,ty=map(int,input().split())
move=[]
for i in range(ty-sy):
    move.append("U")
for i in range(tx-sx):
    move.append("R")
for i in range(abs(sy-ty)):
    move.append("D")
for i in range(abs(sx-tx)):
    move.append("L")
move.append("L")
for i in range(ty-sy+1):
    move.append("U")
for i in range(tx-sx+1):
    move.append("R")
move.append("D")
move.append("R")
for i in range(abs(sy-ty)+1):
    move.append("D")
for i in range(abs(sx-tx)+1):
    move.append("L")
move.append("U")
print("".join(move))