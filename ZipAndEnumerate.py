### zip ###
# zip returns an iterator that combines multiple iterables into one sequence of tuples. 
# Each tuple contains the elements in that position from all the iterables. For example, printing
some_list = list(zip(['a','b','c'], [1,2,3]))
print(some_list)

letters, nums = zip(*some_list)
for c in letters:
    print(c)
for i in nums:
    print(i)

### Enumerate ###
# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. 
# You'll often use this when you want the index along with each element of an iterable in a loop.
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print("{} {}".format(i,letter))
    print(len(letters))

# Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. 
# Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for l, x, y, z in zip(labels, x_coord, y_coord, z_coord ):
    item = str("{}: {}, {}, {}".format(l, x, y, z))
    points.append(item)
    
for point in points:
    print(point)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for l, x, y, z in zip(labels, x_coord, y_coord, z_coord ):
    item = str("{}: {}, {}, {}".format(l, x, y, z))
    points.append(item)
    
for point in points:
    print(point)



print("END")
