my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    new_list = my_list[index]
    index += 1
    if new_list == 0:
        continue
    elif new_list < 0:
        break
    else:
        print(new_list)