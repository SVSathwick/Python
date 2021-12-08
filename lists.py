print('\n')
# fruits = ['apple', 'banana', 'orange', 'pomagranate']
# print(fruits)
# print('type of fruits is {} and total count is {}'.format(type(fruits), len(fruits)))
# for fruit in fruits:
#     print('fruit name is {} and its data type is {}'.format(fruit.capitalize(), type(fruit)))

# list1 = ["abc", 34, True, 40, "male"]
# print('\n')
# print('list of items {}'.format(list1))
# for item in list1:
#     print('item is {} and its data type is {}'.format(item, type(item)))

# print('\n')
# print('list of items {}'.format(list1))
# print('Printing only strings from the above list')
# for item in list1:
#     if type(item) is str:
#         print(item)

# print('\n')
# print('list of items {}'.format(list1))
# print('Printing only intgers from the above list')
# for item in list1:
#     if type(item) is int:
#         print(item)

# print('\n')
# print('list of items {}'.format(list1))
# print('Printing only booleans from the above list')
# for item in list1:
#     if type(item) is bool:
#         print(item)

#list constructor
# fruits = list(("apple", "banana", "cherry", "orange", "kiwi", "mango"))
# print(fruits)
# fruit = 'banana'
# if fruit in fruits:
#     print('{} is present in {}'.format(fruit, fruits))
# else:
#     print('{} is not present in {}'.format(fruit, fruits))

# print('before changing the list\n{}'.format(fruits))
# fruits[1:3]=['black berry', 'custard apple']
# print('after changing the list\n{}'.format(fruits))
# fruits[5]='guava'.capitalize()
# print('after changing the list\n{}'.format(fruits))

# new_fruit = 'straw berry'
# fruits.append(new_fruit)
# print('after appending {} to the list\n{}'.format(new_fruit, fruits))

# fruits.insert(0, 'green banana')
# print('after inserting {} to the list at {}\n{}'.format('green banana', 0, fruits))

skills = ['C', 'C++', 'VB']
print('skills {}'.format(skills))
hot_skills = ['Python', 'Javascript']
print('hot skills {}'.format(hot_skills))
skills.extend(hot_skills)
print('skills after adding hot skills {}'.format(skills))