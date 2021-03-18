"""Teplota ve městech
Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")


Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

Dále napiš následující dotazy:

Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda
Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů
a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.


Pokročilá varianta

Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu
ve stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature.
Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek.
Napravo pak můžeš provádět výpočty pomocí již existujících sloupců.
Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
Nyní můžeš zpracovat následující příklady:

Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu
(sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů.
Jsou některé hodnoty podezřelé?

"""
# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

import pandas
teploty = pandas.read_csv('temperature.csv')
print(teploty.head())


# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního?
print(teploty[teploty['City'] == 'Prague'])
# Hodnoty jsou vysoké - budou to Fahrenheity.


# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(teploty[teploty['AvgTemperature'] > 80])


# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů
# a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe)
print(teploty[(teploty['AvgTemperature'] > 60) & (teploty['Region'] == 'Europe')])


# Dotaz na extrémní hodnoty
print(teploty[(teploty['AvgTemperature'] > 80) | (teploty['AvgTemperature'] < -20)])


# POKROČILÁ VERZE

import pytemperature
teploty["AvgTempCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

print(teploty.head())

# Dotaz na měření, ve kterých je teplota vyšší než 30 stupňů Celsia.
print(teploty[teploty['AvgTempCelsia'] > 30])

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu Evropa.
print(teploty[(teploty['AvgTempCelsia'] > 15) & (teploty['Region'] == 'Europe')])

# Dotaz na extrémní hodnoty
print(teploty[(teploty['AvgTempCelsia'] > 30) | (teploty['AvgTemperature'] < -10)])
# Podezřelé hodnoty jsou z Afriky - určitě neměli - 70°C


