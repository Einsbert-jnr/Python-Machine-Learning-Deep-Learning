# sort() method = used with lists

# sorted() function l= used with iterables
# tuple has no attribute of sort: that's when the sort funtion comes in

students = ["squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort(reverse=True) # key=## is also an optional argument
sorted_students = sorted(students, reverse=False)
print(sorted_students)

for i in students:
    print(i)

students = students = [("squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]
grade = lambda grades: grades[1]
students.sort(key=grade, reverse=False)

for student in students:
    print(student)

students = (("squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

sorted_list = sorted(students, key=grade, reverse=False)

for student in sorted_list:
    print(student)