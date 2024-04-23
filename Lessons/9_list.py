numbers_list = [1, 2, "three", "four", 5, "six"]

numbers_list.append("seven")
numbers_list.remove("seven")
numbers_list.insert(2, 3)

for i in numbers_list:
    print(i)