# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

a = ("Sathwick", 1, "Software Engineer")
(name, empID, designation) = a
print(name)
print(empID)
print(designation)

names = tuple()
heights = tuple()

fruitsTuple = ("Apple", "Orange", "Mango", "Banana")
print("fruitsTuple: ",fruitsTuple)
fruitsTuple2 = "\t".join(fruitsTuple)
print("fruitsTuple2: ", fruitsTuple2)
print("fruitstuple2 TYPE:", type(fruitsTuple2))
print(fruitsTuple[1])
print("fruitsTuple range 1:3 ", fruitsTuple[1:3])
# for item in cast:
#     names.  
#     names.append(item[0])
#     heights.append(item[1])

# define names and heights here
# print(names)
# print(heights)