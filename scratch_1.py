original_dict = {1: 'value1', 2: 'value2'}
new_dict = {v: k for k, v in original_dict.items()}
print(new_dict)

a = [1, 2, 3]
b = ['q', 'w', 'e']
new_dict = {key: value for key, value in zip(a, b)}
print(new_dict)

nested_list = [[1, 2, 3], [4, 5, 6]]
flat_list = []
for item in nested_list:
    flat_list.extend(item)
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = list(set(a + b))
print(new_list)

original_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted_dict = sorted(original_dict.items(), key=lambda x: x[1], reverse=True)
top_list = [item[0] for item in sorted_dict]
top_three = top_list[:3]
print(top_three)