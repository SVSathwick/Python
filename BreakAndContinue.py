manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# Break the String #
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. 
# You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. 
# If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 
# Consider adding print statements to your code to help you resolve bugs.
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
current_length = 0

# for headline in headlines:
#     print("Length of {} : {}".format(headline, len(headline)))
#     if current_length < 140:

#         if (current_length + len(headline)) > 140:

#             news_ticker += " "
#             current_length += 1

#             for i in range(len(headline)):
#                 news_ticker += headline[i]
#                 current_length += 1

#                 if current_length > 140:
#                     break
#         else:
#             if current_length > 0 :
#                 news_ticker += " "

#             current_length += 1

#             for i in range(len(headline)):
#                 news_ticker += headline[i]
#                 current_length += 1
#                 if current_length > 140:
#                     break

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for number in check_prime:
    isPrime = True
    i = 2
    while i < int(number/2):
        if number%i == 0:
            print("{} is not a prime number, because {} is a facotr of {}".format(number, i, number))
            isPrime = False
            break        
        i += 1

    if isPrime:
        print("{} is a prime number".format(number))

print("END")
