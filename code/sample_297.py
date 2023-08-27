x = "this is a pen."
print(x.translate(str.maketrans({"t": "T", " ": None, ".": "!"})))
