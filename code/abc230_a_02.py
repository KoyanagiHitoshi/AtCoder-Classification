N=int(input())
print("AGC"+str(N).zfill(3) if N<42 else "AGC"+str(N+1).zfill(3))