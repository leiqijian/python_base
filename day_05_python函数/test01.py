dict = {}

dict[1] = 1
dict["1"] = 2
dict[1.0] = 3

print(dict[1] + dict["1"] + dict[1.0])
