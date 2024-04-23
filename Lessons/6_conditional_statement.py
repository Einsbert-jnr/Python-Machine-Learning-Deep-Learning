age = int(input("Enter your age:> "))

if age == 100:
    print("You are obolo")
elif 25 >= age > 0:
    print("You are eligible")
elif age >25 or age == -25:
    print("I don't know")
else:
    print("Don't do anything")