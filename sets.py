from typing import Set

#Below is a list
countries = ["India", "Pakistan", "Bangladesh", "India"]

print("type(countries):", type(countries))
print("Countries:", countries)
countries.append("Pakistan")
print("type(countries):", type(countries))
print("Countries:", countries)

#list gets type casted to set thus removing duplicates
#Set works similar to C++'s std::set, except that the elements are not sorted automatically
uniqueCountries = set(countries)
print("type(uniqueCountries):", type(uniqueCountries))
print("uniqueCountries:", uniqueCountries)
uniqueCountries.add("Pakistan")
print("type(uniqueCountries):", type(uniqueCountries))
print("uniqueCountries:", uniqueCountries)

sports = set(["Cricket", "Football", "Tennis", "Cricket", "Boxing"])
print("Type(Sports):", type(sports))
print("Sports", sports)

i = 10
print("Type(i):", type(i))

d = float(10)
print("Type(d):", type(d))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop() #returns a random element. This is stiopwert\\\\

fruits = {"Apple", "orange", "Banana", "Apple"}
print("fruits: ", fruits)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes", "cherry"])
thisset.remove("apple")
print(thisset)

print("END")
