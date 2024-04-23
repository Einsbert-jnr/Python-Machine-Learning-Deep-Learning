# filter()

# filter(function, filter)

friends = [("squidward", 60),
           ("Sandy", 33),
           ("Patrick", 36),
           ("Spongebob", 20),
           ("Mr.Krabs", 78)]

age = lambda data: data[1] >= 40

filtered = list(filter(age, friends))

for i in filtered:
    print(i)