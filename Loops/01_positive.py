numbers = [1, -2, 3, 4, 7, -3, 34, -5, -66, 10, 43, 23, -7, 6, -99]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Total positive numbers in the list are : ", positive_number_count)
