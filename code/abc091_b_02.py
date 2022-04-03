N=int(input())
s=[input() for n in range(N)]
M=int(input())
t=[input() for m in range(M)]
word=list(set(s))
print(max(0,max(s.count(word[i])-t.count(word[i]) for i in range(len(word)))))