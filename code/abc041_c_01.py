N=int(input())
A=[(int(a),i) for i,a in enumerate(input().split(),1)]
for a in sorted(A)[::-1]:
    print(a[1])