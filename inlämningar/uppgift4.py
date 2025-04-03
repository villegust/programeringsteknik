import csv
import matplotlib.pyplot as plt
from math import pi, sin

"""
Uppgift a)
"""

def load_csv(filename):
    rader = []

    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader: 
            rader.append([cell.lower() for cell in row])
            
        result = {p[1]: list(map(float, p[3:])) for p in rader }

    return result

def filter_nordic_data(data):
    nordic_countries = ["dnk", "fin", "isl", "nor", "swe"]
    time = list(range(1960, 2015))
    
    return {country: data[country][2:len(time) + 2] for country in nordic_countries if country in data}

def extended_list(x, n):
    lst = []
    for e in x:
        lst.append(e)

    for _ in range(n):
        lst.insert(0, x[0])
        lst.append(x[len(x)- 1])

    return lst

def smooth_a(x, n):
    res = []
    y = extended_list(x, n)

    for i in range(n, len(y) - n):
        res.append(sum(y[i-n:i+1+n])/ (2*n + 1))

    return res

def smooth_b(x, n):
    res = []

    for i in range(len(x)):
        res.append(sum(x[max(0, i - n):min(len(x), i + n + 1)]) / (min(len(x), i + n + 1) - max(0, i - n)))

    return res

file = "CO2Emissions_filtered.csv"
data = load_csv(file)
nordic_data = filter_nordic_data(data)

for country, values in nordic_data.items():
    print(f"{country} : {values} \n")
    print(f"{country} Smooth_a values: {smooth_a(values, 1)} \n")
    print(f"{country} Smooth_b values: {smooth_b(values, 1)} \n")

