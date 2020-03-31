H,W=map(int,input().split())
S=["."+input()+"." for i in range(H)]
S=["."*(W+2)]+S+["."*(W+2)]
flag=0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            if S[i-1][j]=="." and S[i+1][j]=="." and S[i][j-1]=="." and S[i][j+1]==".":
                flag=1
print("Yes" if flag==0 else "No")