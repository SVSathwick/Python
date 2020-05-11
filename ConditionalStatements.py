phoneBalance = 0
bankBalance = 100

print("Phone Balance: ", phoneBalance)
print("Bank Balance: ", bankBalance)
if phoneBalance < 5:
    phoneBalance += 10
    bankBalance -= 10
print("Phone Balance: ", phoneBalance)
print("Bank Balance: ", bankBalance)

# while phoneBalance < 100:
#     phoneBalance += 10
#     bankBalance -= 10
#     print("Phone Balance: ", phoneBalance)
#     print("Bank Balance: ", bankBalance)

if not True:
    print("TRUE")
else:
    print("FALSE")

seasonsSet = {"spring", "summer", "fall", "winter", "Rainy"}

print("***Printing from Set***")
for season in seasonsSet:    
    if season == 'spring':
        print('plant the garden!')
    elif season == 'summer':
        print('water the garden!')
    elif season == 'fall':
        print('harvest the garden!')
    elif season == 'winter':
        print('stay indoors!')
    elif season == "Rainy":
        print("Carry Umbrella")
    else:
        print('unrecognized season')

seasonsList = ["spring", "summer", "fall", "winter", "Rainy"]
print("***Printing from List***")
for season in seasonsList:    
    if season == 'spring':
        print('plant the garden!')
    elif season == 'summer':
        print('water the garden!')
    elif season == 'fall':
        print('harvest the garden!')
    elif season == 'winter':
        print('stay indoors!')
    elif season == "Rainy":
        print("Carry Umbrella")
    else:
        print('unrecognized season')


for i in range(1, 10):
    if i%2 == 0:
        print("Number {} is even".format(i))
    else:
        print("Number {} is odd".format(i))