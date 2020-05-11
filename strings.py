# my_string = "venkata sathwick sivvala"
# print(my_string)

# print("Capitalize: " + str.capitalize(my_string))
# # print("encode: " + str.encode(my_string))
# nBikes = 1
# nCars = 0
# print("Sathwick has {} bikes and {} cars".format(nBikes, nCars))

# animal = "dog"
# action = "bite"
# print("Does your {} {}?".format(animal, action))

# details = "Sathwick lived in {} for {} years"
# city = "Pune"
# noOfYears = 5.5
# print(details.format(city, noOfYears))

# name = "Sathwick"
# print(name.endswith('i'))
# print(name.startswith('S'))

# txt = "This is a Sample String"
# print(txt.casefold())

# print("No of a's in txt: ", txt.count('a'))

# print("Enoded result: ", txt.encode())

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# print(txt.encode(encoding="ascii",errors="strict"))