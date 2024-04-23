import os

path = 'text.tx'

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print(f"{path} is a file")
    elif os.path.isdir(path):
        print(f"{path} is a directory")
    else:
        print(f"{path} is something else I know nothing about")
else:
    print("That location doesn't exits")