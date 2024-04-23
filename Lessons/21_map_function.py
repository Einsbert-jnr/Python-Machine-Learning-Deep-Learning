# map()
# map(function, iterable)

store = [("squidward", 60),
         ("Sandy", 33),
         ("Patrick", 36),
         ("Spongebob", 20),
         ("Mr.Krabs", 78)]

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(f"{i}")