# walrus operator (:=) also called assignment operator

happy = True
print(happy)

# simple way of writing the above code
print(happy := True)

# while loop example
foods = list()

while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

# simple way of writing above code

while food := input("What is food do you like? ") != "quit":
    foods.append(food)