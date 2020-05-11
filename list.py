months = ["January", "February", "March", "April", "may", "June", "July", "August", "September", "October", "November", "December"]
print(months[0])
print(months[2])

firstHalf = months[:6]
print(firstHalf)

Q1 = months[0:3]
print("Q1:", Q1)
Q2 = months[3:6]
print("Q2:", Q2)
Q3 = months[6:9]
print("Q3:", Q3)
Q4 = months[9:12]
print("Q4:", Q4)

list_of_random_things = [1, "Sathwick", 12.5]
print(list_of_random_things[0])
print(list_of_random_things[1])
print(list_of_random_things[2])

print("January" in months)

my_list = [1,2,3,4,5]
print("MyList: ", my_list)
my_list[0] = "Hello"
print("MyList: ", my_list)
my_list = "Hi"
print("MyList: ", my_list)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
#case 1: Works like reference type. If one list's contents changes other list also gets effected
list2 = list1
#case 2: copies entire contents of the right side to left. Both are independent now
#list2 = list1.copy()
print("list1", list1)
print("list2", list2)
list2[4] = 4
print("list1", list1)
print("list2", list2)

names = ["Sathwick", "Sunitha", "Anshuman", "Santosh", "Suresh", "Anil", "Naresh"]
print("Names: ", names)
print("Total Names: ", len(names))
print("Max: ", max(names))
print("Min: ", min(names))
sortedNames = sorted(names)
print("Sorted names: ", sortedNames)

names.append("Rajesh")
print("Names: ", names)

sortedNames.append("Rajesh") #This will not sort the list again. The new item will be added at the end of sorted list.
print("SortedNames: ", sortedNames)

# join() method :Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
new_str = "\t".join(["fore", "aft", "starboard", "port"])
print(new_str)
new_str2 = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str2)

joined_names_tab = "\t".join(sorted(names))
print("joined_names_tab: ",joined_names_tab)

joined_names_tab_2 = "\t".join(["Sathwick", "Sunitha", "Anshuman", "Santosh", "Suresh", "Anil", "Naresh"])
print("joined_names_tab_2", joined_names_tab_2)

joined_names_new_line = "\n".join(sorted(names))
print("joined_names_new_line:\n",joined_names_new_line)

joined_names_dash = "-".join(sorted(names))
print("joined_names_dash: ",joined_names_dash)

#append method
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

characters = ['a', 'b', 'c']
characters.append('d')
print(characters)

for i in range(3):
    print("i(inside loop): {}".format(i))
print("i(onside loop): {}".format(i))

print("End")
