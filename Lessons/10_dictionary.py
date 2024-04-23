# dictionary = A changeable, unordered collection of unique key:value pairs. fast because they use hashing, allow us to access a value quickly.

capitals = {'USA': 'washington DC',
            'India':'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals["Russia"]) # Can interrupt the flow of the program if the key isn't in the dictionary

capitals.update({"Russia": "Moscow"})
print(capitals.get("Russia"))

for key, value in capitals.items():
    print(f"{key}:> {value}")