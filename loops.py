cities = ["New York", "Atlanta", "Boston", "Orlando", "Miami", "Tampa", "Dayton", "Huntsville"]
# for city in cities:
#     print(city.title())

# for city in cities:
#     print(city)

cities.sort()
# for city in cities:
#     city = city.upper()
#     print(city.upper())

# for city in cities:
#     print(city.title())

# cities.insert(1, "New Jersey")
# for city in cities:
#     print(city.title())

totalCities = len(cities)
# city = 0
# while city < totalCities:
#     print(cities[city])
#     city += 1

# for i in range(0, totalCities, 3):
#     print(cities[i])

# for i in range(3):
#     print("HELLO")

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

# write your for loop here
# for name in names:
#     username = name.lower()
#     username.replace(" ", "_")
#     usernames.append(username)

# print(usernames)

# # Modify Usernames with Range
# usernames2 = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# # write your for loop here
# for i in range(len(usernames2)):
#     usernames2[i] = usernames2[i].lower().replace(" ","_")

# print(usernames2)


# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# count = 0

# # write your for loop here
# for token in tokens:
#     if token.startswith('<') and token.endswith('>'):
#         count += 1

# print(count)

# print(list(range(0,-5)))

bookTitle =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
wordCounter = {}

# for word in bookTitle:
#     if word not in wordCounter:
#         wordCounter[word] = 1
#     else:
#         wordCounter[word] += 1

# for word in bookTitle:
#     wordCounter[word] = wordCounter.get(word, 0) + 1

print(wordCounter)

# countryCapitals = {("India", "New Delhi"), ("Pakistan","Islamabad")}
# print(type(countryCapitals))
# print(countryCapitals)

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print("Key: {}, value: {}".format(key, cast[key]))

# print("\nIterating through keys and values:")
# for key, value in cast.items():
#     print("Actor: {}    Role: {}".format(key, value))

for i in range(10):
    name = "Sathwick"
    print("Name(inside loop): ", name)
    print("Inside loop: ", i)

# Here the variable i and name declared inside loop are not local  ***WEIRD***
print("Name(outisde loop): ", name)
print("Outside loop: ", i)

print("END")