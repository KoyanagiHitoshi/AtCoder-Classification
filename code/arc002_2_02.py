import datetime
day=datetime.datetime.strptime(input(),"%Y/%m/%d")
while day.year%(day.month*day.day)!=0:
    day+=datetime.timedelta(days=1)
print(day.strftime("%Y/%m/%d"))