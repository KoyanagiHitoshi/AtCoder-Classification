import datetime
Y,M,D=map(int,input().split("/"))
day=datetime.date(Y,M,D)
while Y%(M*D)!=0:
    day=datetime.date(Y,M,D)+datetime.timedelta(days=1)
    Y,M,D=day.year,day.month,day.day
print(day.strftime("%Y/%m/%d"))