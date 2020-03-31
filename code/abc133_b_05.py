import numpy as np
N,D=map(int,input().split())
X=np.array([list(map(int,input().split())) for i in range(N)])
print(sum(1 for i in range(N) for j in range(i+1,N) if np.linalg.norm(X[i]-X[j]).is_integer()))