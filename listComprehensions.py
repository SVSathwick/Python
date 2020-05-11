cities = ["hyderabad", "bangalore", "chennai", "pune", "delhi"]
print(type(cities))

capitalized_cities = list()
for city in cities:
    capitalized_cities.append(city.title())

print(cities)
print(capitalized_cities)

#using list comprehensions
capitalized_cities1 = [city1.title() for city1 in cities]
print(cities)
print(capitalized_cities1)

squares = list()
for x in range(9):
    squares.append(x*x)

print(squares)

#using list comprehensions
squares1 = list()
squares1 = [x*x for x in range(20) if x%2 == 0]
print(squares1)

squares_and_cubes = list()
squares_and_cubes = [x**2 if x%2==0 else x**3 for x in range(20)]
print(squares_and_cubes)

#QUIZ
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [(first_name.split(" ", 1)[0]).lower() for first_name in names]
print(first_names)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
print(type(scores))