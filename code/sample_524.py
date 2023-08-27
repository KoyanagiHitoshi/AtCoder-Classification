x = "abc"
[print(chr(i), end=" ") for i in range(ord("a"), ord("z")+1) if chr(i) in x]
