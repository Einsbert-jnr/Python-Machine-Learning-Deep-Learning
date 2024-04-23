import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(0.00031)

print('Hurray!!!!!!!!!!!!!!!!....It\'s your birthday')

# nested loop
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for row in range(rows):
    for column in range(columns):
        print(symbol, end="")
    print()