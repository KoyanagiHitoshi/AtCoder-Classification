import numpy as np
N=int(input())
A=list(map(int,input().split()))
cum=np.cumsum(A)
cut=np.append([0,360],cum%360)
diff=np.diff(sorted(cut))
print(np.max(diff))