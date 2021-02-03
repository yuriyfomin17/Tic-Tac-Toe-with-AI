string = input()
new_list = [x for x in string.split(" ") if x.endswith("s")]

print("_".join(new_list))