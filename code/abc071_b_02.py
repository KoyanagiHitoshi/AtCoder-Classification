S=input()
print(min(set(map(chr,range(97,123)))-set(S) or ["None"]))