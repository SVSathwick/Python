#Keys are auto sorted in Dictionaries similar to std::map in C++
elements = {'Hydrogen':1, "Helium":2, "Oxygen":3}
elements["Hydrogen"] = 4
elements["Hello"] = 5
print(elements["Helium"])
poppedItem = elements.popitem()
print(poppedItem)
print(elements)

print("Oxygen" in elements)
print("Helium" in elements)
if "Hydrogen" in elements:
    print("Hydrogen is present")

if not "Hello" in elements:
    print("Hello is not present")

#Keys must be unique
#If there are duplicates, latest value will be assigned
employees = {1:"Sathwick", 2:"Guru", 3:"Manju", 4:"Venkat", 1:"ABC"}
for id in employees.keys():
    print("Employee id: {}, name: {}".format(id, employees[id]))
    print("Name: {}".format(employees.get(id)))

for i in range(0, 5):
    value = employees.get(i)
    if value is not None:
        print("id: {}, name: {}".format(i, value))
    else:
        print("No value for {}".format(i))

for name in employees.values():
    print("Name: {}".format(name))

cities = {"Mumbai":12.5, "Hyderabad":7.5, "Chennai":8.5, "Pune":5.5}
populationInMumbai = cities.get("Mumbai")
print("Population in Mumbai", populationInMumbai)

#returns None when key is not present
populationInBangalore = cities.get("Bangalore")
print("Population in Bangalore: ",populationInBangalore)

#returning default value if key is not present
populationInVizag = cities.get("Vizag", 5)
print("Population in Vizag", populationInVizag)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# == returns True if contents are same
# is returns True if both the variables are referring to the same object
print(a == b) #True
print(a is b) #True
print(a == c) #True
print(a is c) #False

animals = {'dogs': [20, 10, 15, 8, 32, 15], 
            'cats': [3,4,2,8,2,4], 
            'rabbits': [2, 3, 3], 
            'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals)

print("The result of animals['dogs'][3]", animals["dogs"][3])
#print("The result of animals[3]", animals[3]) #Error

totalDogs = 0
for value in animals["dogs"]:
    totalDogs += value
print("Total Dogs:{}".format(totalDogs))

totalRabbits = 0
for value in animals["rabbits"]:
    totalRabbits += value
print("Total Rabbits:{}".format(totalRabbits))

print("END")