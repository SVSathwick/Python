ford_ecosport = {
    "make" : "Ford",
    "model" : "Ecosport Trend 1.5L Petrol",
    "Mfg Year": 2021,
    "Price" : 857000
}

ford_figo = {
    "make" : "Ford",
    "model" : "Figo Trend 1.2L Petrol",
    "Mfg Year": 2021,
    "Price" : 585000
}

tata_nexon = {
    "make" : "Tata",
    "model" : "Nexon XZA 1.2L Turbo Petrol",
    "Mfg Year": 2021,
    "Price" : 857000
}
cars = [ford_ecosport, ford_figo, tata_nexon]

mahindra_xuv300 = {
    "make" : "Mahindra",
    "model" : "XUV W8 1.2L Turbo Petrol",
    "Mfg Year": 2020,
    "Price" : 900000
}
cars.append(mahindra_xuv300)

def print_cars(cars):
    for car in cars:
        print(car)

print_cars(cars)

def cars_mfg_in_2020(cars):    
    cars2020 = list()
    for car in cars:
        if(car["Mfg Year"] == 2020):
            cars2020.append(car)
        
    return cars2020

cars2020 = cars_mfg_in_2020(cars)
print('\nCars manufactured in 2020:\n{}'.format(cars2020))

for car in cars:
    if car.get("model") == "Figo Trend 1.2L Petrol":
        car["Mfg Year"] = 2020

cars2020 = cars_mfg_in_2020(cars)
print('\nCars manufactured in 2020:\n{}'.format(cars2020))