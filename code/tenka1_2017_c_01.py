N=int(input())
for h in range(1,3501):
    for n in range(h,3501):
        if 4*h*n>N*n+N*h:
            w=(N*h*n)/(4*h*n-N*n-N*h)
            if w==int(w):
                print(h,n,int(w))
                exit()