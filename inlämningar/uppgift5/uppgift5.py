
"""
Den här filen kan ni använda för att testa att din kod för klassen Temperature är
korrekt,
innan du tillämpar den på de riktiga fallen
"""
from weather import Temperature
from matplotlib import pyplot as plt
# Filen innehåller temperaturen för de 15 första dagarna i 2021
filename = "smhi-temp-2021-kort.csv"
#
t2021 = Temperature(filename)
print(t2021)
# Antal datapunkter i smhi-temp-2021-kort.csv är 355 stycken.
#
t2021_max,t2021_max_tidpunkt = t2021.max_value()
print(f"Högsta temperatur {t2021_max} grader Celsius den {t2021_max_tidpunkt[0:10]} kl {t2021_max_tidpunkt[-2:]}\n")
#Högsta temperatur 2.2 grader Celsius den 2021-01-01 kl 00
#
t2021_min,t2021_min_tidpunkt = t2021.min_value()
print(f"Lägsta temperatur {t2021_min} grader Celsius den {t2021_min_tidpunkt[0:10]} kl {t2021_min_tidpunkt[-2:]}\n")
#Lägsta temperatur -13.6 grader Celsius den 2021-01-15 kl 09
antal_timmar = 24
smooth = t2021.smoothing(antal_timmar)
print(f' Utan {t2021.temperature[0:4]}')
print(f' Med {smooth[0:4]}')
#Timvis [2.2, 0.9, 1.0, 1.5]
#Mededlvärde per dygn [0.9520000000000001, 0.9615384615384616, 0.9629629629629629, 0.9535714285714285]
fig,ax = plt.subplots()
#Figure 1:
ax.plot(t2021.time,t2021.temperature,linestyle = '-',color='blue',label='Timvis')
ax.plot(t2021.time,smooth,linestyle='-',color='red',label = 'Medelvärde')
ax.set_title(f'Temperatur i Kåbo')
ax.set_xlabel(f'Tidpunkt')
ax.set_ylabel(f'Temperatur (C)')
plt.show()
