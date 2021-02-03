seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
new_list = [int(x / 86400) for x in seconds]

print(new_list)
