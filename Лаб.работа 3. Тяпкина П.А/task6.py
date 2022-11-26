list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ind = 0
max_ = list_numbers[0]
for i in range(len(list_numbers)):
    if list_numbers[i] >= max_:
        max_ = list_numbers[i]
        max_ind = i
list_numbers[-1], list_numbers[max_ind] = list_numbers [max_ind],list_numbers[-1]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
