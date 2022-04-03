N=int(input())
s=[input() for i in range(N)]
M=int(input())
t=[input() for i in range(M)]
card=list(set(s))
print(max(0,max(s.count(card[i])-t.count(card[i]) for i in range(len(card)))))