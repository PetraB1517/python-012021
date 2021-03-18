"""Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubr obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

Stažení souboru pomocí wget:
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu.
Pandas ti tuto hodnotu vrací jako číslo.
Načti si tedy první hodnotu zavírací ceny (sloupec Close) v souboru a poslední hodnotu zavírací ceny v souboru.
Vypočítej, o kolik procent se zvýšila hodnota akcie.

Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii.
Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období.
Obdobným způsobem použij funkci .min() na sloupec Low.
Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (price range).
"""
import pandas
twilio = pandas.read_csv('twlo.csv')

# Zjisti, kolik má soubor řádek a kolik sloupců.
print(twilio.shape)

# U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
print(twilio.iloc[-1])

# Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
print(twilio.iloc[:5])
print(twilio.head())

# Počet řádků ulož do proměnné pocet_radku jako číslo.
pocet_radku = int(twilio.shape[0])

# Zvýšení akcie
akcie_last = twilio.iloc[-1][-1]
akcie_first = twilio.iloc[0][-1]
zvyseni_akcie = round((akcie_last - akcie_first)*100/akcie_first)/100
print("Hodnota akcie se zvýšila o " + str(zvyseni_akcie) + " %.")

# Price range
price_range = round((twilio.iloc[:, 3].max() - twilio.iloc[:, 4].min())*100)/100

print("Maximální rozsah obchodní ceny akcie je " + str(price_range))