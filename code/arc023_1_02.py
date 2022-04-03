Y=int(input())
M=int(input())
D=int(input())
if M==1 or M==2:
    Y-=1
    M+=12
print(735369-(365*Y+Y//4-Y//100+Y//400+306*(M+1)//10+D-429))