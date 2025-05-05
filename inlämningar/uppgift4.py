import csv
import matplotlib.pyplot as plt

#Global variabel som används av olika funktioner.
time = list(range(1960, 2015))

def load_csv(filename):
    rader = []

    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            rader.append([cell.lower() for cell in row])

        result = {p[1]: list(map(float, p[3:])) for p in rader}

    return result

def extended_list(x, n):
    """
    Funktion som skapar en lista där de element utanför listan är de första och sista index i listan.
    """
    lst = []
    for e in x:
        lst.append(e)

    for _ in range(n):
        lst.insert(0, x[0])
        lst.append(x[len(x)- 1])

    return lst

def smooth_a(x, n):
    """
    Returnerar en utjämnad version av listan x med glidande medelvärde över 2n + 1 värden.
    Listan utökas först i kanterna med hjälp av extended_list.
    """
    res = []
    extended_lst = extended_list(x, n)

    for i in range(n, len(extended_lst) - n):
        res.append(sum(extended_lst[i - n:i + n + 1])/ (2*n + 1))

    return res

def smooth_b(x, n):
    """
    Funktion som utför en medelvärdesutjämning på en lista x.
    
    För varje element i listan beräknas medelvärdet av elementet själv samt n element före
    och n element efter (så långt som möjligt inom listans gränser)
    """
    res = []

    for i in range(len(x)):
        res.append(sum(x[max(0, i - n):min(len(x), i + n + 1)]) / (min(len(x), i + n + 1) - max(0, i - n)))
    
    return res

data = load_csv("CO2Emissions_filtered.csv")

countries = [["dnk", "blue"], ["fin", "orange"], ["isl", "green"], ["nor", "red"], ["swe", "purple"]]
fig, ax = plt.subplots()

for i in countries:
    ax.plot(data[i[0]], linestyle=":", color=i[1])
    ax.plot(smooth_a(data[i[0]], 1), linestyle="-", color=i[1])
    ax.plot(smooth_b(data[i[0]], 1), linestyle="--", color=i[1])


ax.set(xlabel="Year", ylabel="CO2 Emissions (kt)", title="Yearly Emissions of CO2 in the Nordic Countries")

plt.show()