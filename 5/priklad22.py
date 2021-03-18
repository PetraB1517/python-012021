"""Hra o trůny
Stáhni si soubor character-deaths.csv, která obsahuje informace o smrti některých postav z prvních pěti knih
 románové série Píseň ohně a ledu (A Song of Fire and Ice).

Stažení souboru pomocí wget:

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

Pozn. Úkoly se týkají zcela nevýznamných postav, proto je riziko spoileru minimální :-)
Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom,
jestli se v knize postava vyskytuje.
Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom,
v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.
"""
# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.

import pandas

mrtvoly = pandas.read_csv('character-deaths.csv')
mrtvoly = mrtvoly.set_index('Name')

# Zobraz si sloupce, které tabulka má.
# Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
print(mrtvoly.columns)

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".

print(mrtvoly.loc['Hali'])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".

print(mrtvoly.loc['Gevin Harlaw': 'Gillam'])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.

print(mrtvoly.loc['Gevin Harlaw': 'Gillam', 'Death Year'])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom,
# v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.

print(mrtvoly.loc['Gevin Harlaw': 'Gillam', 'GoT':'DwD'])
