# list comprehension
# list = [expression for item in iterable]

# dictionary comprehension
# dict = {key: expression for it (key, value) in iterable.items}
# It takes the same format as that of list comprehension
square = []

for i in range(1, 11):
    square.append(i * i)
print(square)

# list comprehension format
square = [i * i for i in range(1, 11)]
print(square)

# adding conditional statements to a list comprehenshion
student = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
passed_student = [i for i in student if i >= 50]
total_response = [i if i >= 50 else "Failed" for i in student]
print(total_response)
print(passed_student)