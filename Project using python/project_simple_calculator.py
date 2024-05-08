# Trying to build a calculator

def welcome():
    print("Choose the operation you want to perform")
    print("A --> Addition")
    print("B --> Subtraction")
    print("C --> Division")
    print("D Multiplication")


def common():
    number = input("How many numbers do you want to work with? ")
    num_list = []
    for i in range(int(number)):
        num = int(input("Enter the numbers: "))
        num_list.append(num)
    return num_list


def add_and_sub(num):
    summ = 0
    for i in num:
        summ += i
    return summ


def multiply(num):
    summ = 1
    for i in num:
        summ = summ * i
    return summ


value = True

while value:
    welcome()
    # print()
    response = input(">>").lower()
    if response == 'a' or response == 'b':
        outcome = common()
        total = add_and_sub(outcome)
        print()
        print(f"Result: {total}")
        print()

    elif response == 'd':
        outcome = common()
        total = multiply(outcome)
        print()
        print(f"Result: {total}")
        print()

    elif response == 'c':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        total = num1 / num2
        print()
        print(f"Result: {total}")
        print()

    else:
        print("Thanks!!!")
        print("Good bye:)")
        value = False