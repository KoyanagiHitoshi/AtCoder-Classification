import re
s=input()
if re.match("^keyence.*",s) or re.match(".*keyence$",s) or re.match("^k.*eyence$",s)  or re.match("^ke.*yence$",s) or re.match("^key.*ence$",s) or re.match("^keye.*nce$",s) or re.match("^keyen.*ce$",s)or re.match("^keyenc.*e$",s) or re.match("^keyence$",s) :
    print("YES")
else:print("NO")