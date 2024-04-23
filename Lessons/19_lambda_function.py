# lambda function
# lambda parameters: expression

mul = lambda x: x * 2
add = lambda x, y: x + y
name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(age_check(30))
print(name("Hello", "Bro"))
print(add(2, 5))
print(mul(5))