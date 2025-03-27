import csv

with open("CO2Emissions_filtered.csv", "r") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)