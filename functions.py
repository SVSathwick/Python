def calcCylinderVolume(height, radius):
    pi = 3.14159
    return height*pi*(radius**2)

cylinderVolume = calcCylinderVolume(10,30)
print("Cylinder Volume of height({}) and width({}) : {}".format(10,3,cylinderVolume))

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(show_plus_ten(5)))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

def calcCylinderVolume1(height, radius=5):
    pi = 3.14159
    return height*pi*(radius**2)

print(calcCylinderVolume1(10,5))
print(calcCylinderVolume1(10))

# write your function here



def population_density(population, area):
    return population/area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# write your function here
def readable_timedelta(days):
    noOfWeeks = days//7
    noOfDays = days%7
    return "{} weeks(s) and {} day(s).".format(noOfWeeks, noOfDays)

# test your function
print(readable_timedelta(1))

def reverseAString(str):
    return str[::-1]

myName = "My Name is Venkata Sathwick Sivvala"
print(reverseAString(myName))

def reverseWords(str):
    print(myName)
    retStr = ""
    strArray = str.split()
    i=len(strArray)-1
    while(i>=0):
        retStr += strArray[i] + " "
        i += -1

    return retStr

myName2 = "My name is Sunitha Duppada"
print(reverseWords(myName2))


# def add(val1, val2, val3):
#     return val1+val2+val3
    
# val1 = 1
# val2 = 2
# val3 = 3

# result2= add(val1, val2, val3)
# print("Addition of {}, {} and {} is {}".format(val1, val2, val3, result2))