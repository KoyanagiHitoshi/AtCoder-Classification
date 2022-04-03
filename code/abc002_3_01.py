xa,ya,xb,yb,xc,yx=map(int,input().split())
a=((xa-xb)**2+(ya-yb)**2)**.5
b=((xb-xc)**2+(yb-yx)**2)**.5
c=((xc-xa)**2+(yx-ya)**2)**.5
s=(a+b+c)/2
print((s*(s-a)*(s-b)*(s-c))**.5)