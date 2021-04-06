"""Státy světa potřetí
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
Zkusme nyní zpracovat podobné úlohy pomocí pandas.


"""
#Načti data ze souboru do tabulky.
import pandas
staty = pandas.read_json('staty.json')

print(staty)

#Vyfiltruj státy, které leží v Evropě.
staty_evropy = staty.loc[staty['region'] == "Europe"]
print(staty_evropy.head())

#Zjisti počet států v jednotlivých subregionech Evropy.
print(staty_evropy.groupby('subregion')['name'].count())

#Zjisti celkový počet obyvatel v jednotlivých subregionech Evropy.
print(staty_evropy.groupby('subregion')['population'].sum())

#Rozšíření zadání
"""
V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP)
států za roky 2017-2019 ze Světové banky.
"""

#Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP
#tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
gdp = pandas.read_csv('gdp.csv')
gdp = gdp[gdp['2017'].notnull()]
gdp = gdp[gdp['2018'].notnull()]
gdp = gdp[gdp['2019'].notnull()]

#Propoj obě tabulky podle třípísmenného kódu států.
staty = staty.rename(columns={'alpha3Code':'Country Code'})
staty_gdp = pandas.merge(gdp, staty, on=['Country Code'])

#Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
staty_gdp_vyber = staty_gdp.groupby('subregion').agg({"2019": "sum","population": "sum"})
staty_gdp_vyber = staty_gdp_vyber.rename(columns={'2019':'Celkový HDP 2019', 'population':'Celková populace'})
print(staty_gdp_vyber)

"""Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst).
K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele,
tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu."""

staty_gdp_vyber["GDP2019/osoba"] = staty_gdp_vyber["Celkový HDP 2019"] / staty_gdp_vyber["Celková populace"]

print(staty_gdp_vyber)


