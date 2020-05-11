#tuples are immutable
#we can't add new items and can't sort them

employee = (1, "Sathwick")
print(type(employee))
print("Employee id: {}, name: {}".format(employee[0], employee[1]))

# unpacking tuple
id, name = employee
print("Unpacked Employee id: {}, name: {}".format(id, name))

fruitsTuple = ("Apple", "Orange", "Mango", "Banana")
print("fruitsTuple: ",fruitsTuple)
fruitsTuple2 = "\t".join(fruitsTuple)
print("fruitsTuple2: ", fruitsTuple2)
print("fruitstuple2 TYPE:", type(fruitsTuple2))
print(fruitsTuple[1])
print("fruitsTuple range 1:3 ", fruitsTuple[1:3])

# fruitsList = ["Apple", "Orange", "Mango", "Banana"]
# print("fruits-LIST: ",fruitsList)
# print(fruitsList[0])

#convert tuple to list, so that we can change the contents
fruitsList = list(fruitsTuple)
fruitsList[0] = "Kiwi"
print("fruitsList: ",fruitsList)
#fruitsTuple will still hold old values. Copy by value happens here
print("fruitsTuple: ",fruitsTuple)


#iterate through the tuple
for it in fruitsTuple:
    print(it, ", type: ", type(it))
    it = "Pomagranate" #fruitsTuple unchanged
    print(it)

i = 0
while(i<2):
    print(fruitsTuple[i])
    i += 1

it = "iterator"
print(it, ", type", type(it))

#Check if Item Exists
if "Apple" in fruitsTuple:
    print("Apple exitsts")
else:
    print("Apple doesn't exitst")

if "apple" in fruitsTuple:
    print("apple exists")
else:
    print("apple doesn't exitst")

#Create Tuple With One Item
#One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1+tuple2
print(tuple3)

sports = ("Cricket", "Football", "Tennis")
print("Sports: ", sports)
del sports

#below raise an error because the tuple no longer exists
#print sports

print("END")