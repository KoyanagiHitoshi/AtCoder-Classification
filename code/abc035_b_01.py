S=input()
T=int(input())
distance=abs(S.count("L")-S.count("R"))+abs(S.count("U")-S.count("D"))
question=S.count("?")
if T==1:
    print(distance+question)
else:
    print(max(len(S)%2,distance-question))