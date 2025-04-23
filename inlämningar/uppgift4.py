import csv
import matplotlib.pyplot as plt

#Global variabel som används av olika funktioner.
time = list(range(1960, 2015))

def load_csv(filename):
    rader = []

    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            rader.append([cell.lower() for cell in row])

        result = {p[1]: list(map(float, p[3:])) for p in rader}

    return result

def filter_nordic_data(data):
    nordic_countries = ["dnk", "fin", "isl", "nor", "swe"]
    return {country: data[country][2:len(time) + 2] for country in nordic_countries if country in data}

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

file = "CO2Emissions_filtered.csv"
data = load_csv(file)
nordic_data = filter_nordic_data(data)

for country, values in nordic_data.items():
    print(f"{country} : {values} \n")
    print(f"{country} Smooth_a values: {smooth_a(values, 1)} \n")
    print(f"{country} Smooth_b values: {smooth_b(values, 1)} \n")

    """
    Massa matplotlib bullshit
    """

    
    smooth_a_vals = smooth_a(values, 1)
    smooth_b_vals = smooth_b(values, 1)

    def fix_length(lst, target=55):
        if len(lst) < target:
            return lst + [lst[-1]] * (target - len(lst))
        else:
            return lst[:target]

    values_fixed = fix_length(values)
    smooth_a_fixed = fix_length(smooth_a_vals)
    smooth_b_fixed = fix_length(smooth_b_vals)

    plt.plot(time, smooth_a_fixed, label=f"{country}")
    plt.plot(time, values_fixed, linestyle="--")
    plt.plot(time, smooth_b_fixed, linestyle=":")

plt.title("CO₂ Emissions for Nordic Countries (1960–2014)")
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()