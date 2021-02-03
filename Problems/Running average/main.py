number = input()
number = list(number)
new_list = [int(n) for n in number]
# for x in range(1, len(number)):
#     new_list.append((int(number[x]) + int(number[x - 1]))/2)
# print(new_list)
print([(new_list[x] + new_list[x + 1]) / 2 for x in range(len(new_list) - 1)])
