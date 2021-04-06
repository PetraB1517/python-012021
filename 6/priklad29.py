"""Teplota ve městech potřetí
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech
v listopadu 2017.

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
"""

import pandas
teploty = pandas.read_csv('temperature.csv')

# Vyfiltruj si informace o teplotách 13. listopadu 2017.
teploty13 = teploty.loc[teploty["Day"] == 13]

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.

teploty13 = teploty13[teploty13.AvgTemperature > -90]


# Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
print(teploty13.groupby('Region')['Day'].count())

# Vypočti průměrnou teplotu za jednotlivé regiony.
print(teploty13.groupby('Region')['AvgTemperature'].mean())

# Vypočti maximální a minimální teplotu v každém regionu.
print(teploty13.groupby('Region').agg({'AvgTemperature': ["max", "min"]}))