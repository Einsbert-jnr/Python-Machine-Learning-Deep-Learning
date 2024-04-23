# zip(*iterables)
# It aggregate elements from two or more iterables ( list, tuples, sets, etc).

usernames = ["Kojo", "Asante", "Einsbert"]
passwords = ["passwd", "my password", "einsbert@123"]
password = ("passwd", "my password", "einsbert@123")

users = dict(zip(usernames, password))

for key, value in users.items():
    print(f"{key} : {value}")