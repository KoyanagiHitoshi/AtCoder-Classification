X, Y = input().split(".")
print(X+"-" if int(Y) < 3 else X if int(Y) < 7 else X+"+")