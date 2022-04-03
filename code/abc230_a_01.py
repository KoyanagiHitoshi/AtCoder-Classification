N=int(input())
print("AGC{:0=3}".format(N) if N<42 else "AGC{:0=3}".format(N+1))