first_name = "Einsbert"
last_name = "junior"
full_name = first_name + " " + last_name

print("Hello " + full_name)

age = 200
print("Your age is: " + str(age))

height = float(20.5)
print("This is your height: " + str(height) + "cm")

human = False
isHuman = True

print()
print()

# Multiple assignment in python

name, age, height, Male = "Spongebob", 30, 20.5, True
print(f"""Hello {name}! 
You are {age} years old. 
You have a height of {height}cm
{Male}""")

localone = localtwo = localThree = height
print(localone, localtwo, localThree)