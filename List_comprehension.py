# Task_1
numbers_list = [3,5,45,97,32,22,10,19,39,43]

new_list = []
for number in numbers_list:
    if number % 2 == 0:
        new_list.append(number)
print(new_list)
# or
new_list = [number for number in numbers_list if number % 2 == 0]
print(new_list)


# Task_2
mixed_list = [1, 646, 'apple', 'one']

number_list = [str(number) for number in mixed_list if isinstance(number, int) or  isinstance(number, str) and number.isdigit()]
print(number_list)