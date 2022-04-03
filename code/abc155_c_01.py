N=int(input())
S=[input() for i in range(N)]
dictionary={}
for word in S:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
maximum=max(dictionary.values())
for key,value in sorted(dictionary.items()):
    if value==maximum:
        print(key)