import math

# number = int(input())
# n = 1
# new_list = []
# space = 0
# for x in range(number):
#     space = max(space, (len("#" * n) - 1) / 2)
#     new_list.append("#" * n)
#     n += 2
# for x in range(len(new_list)):
#     curr_string = new_list[x].rjust(int(space) + len(new_list[x]), " ")
#     curr_string = curr_string.ljust(int(space) + len(curr_string), " ")
#     space -= 1
#     print(curr_string)

high = int(input())
length = high * 2 - 1
text = '#'
while high:
    print(text.center(length))
    text += '##'
    high -= 1
