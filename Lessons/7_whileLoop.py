"""
Project thesis
    Writing a simple program to do something when you enter your name but continue to prompt you to enter your name if the name field is empty.
"""

# one way
name = ""

while not name:
    name = input("Enter your name:> ")

print(f"Hello {name}")
print("You passed the text")