import math
W=int(input())
s="DiscoPresentsDiscoveryChannelProgrammingContest2016"
for i in range(math.ceil(len(s)/W)):
    print(s[W*i:W+W*i])