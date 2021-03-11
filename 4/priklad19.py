"""Instalace modulu
Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně, ale umí si kurz měny stáhnout z internetu.

Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()).
Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK.
Následně od uživatele získej i požadované množství cílové měny. Nezapomeň toho množství převést na typ int."""


from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovana_mena = input("Na jakou měnu chcete na CZK převést? (zkratka) ")
pozadovano_v_cilove_mene = int(input("Cílové množství požadované měny: "))

cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)
print("Je potřeba " + str(cena_v_korunach) + " Kč")


"""Pokročilejší varianta
Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí,
například převod měny do Bitcoinu. Zkus pomocí modulu vytvořit program, který se zeptá uživatele na měnu
a požadovaný počet Bitcoinů a vrátí mu množství měny, které by potřeboval,
aby požadované množství Bitcoinů mohl koupit."""

from forex_python.bitcoin import BtcConverter

prevodnik = BtcConverter()


zadana_mena = input("Jakou měnu chcete na Bitcoiny převést? (zkratka) ")
pozadovano_v_btc = int(input("Cílové množství Bitcoinů: "))
prevodnik.get_latest_price(zadana_mena)
cena = prevodnik.convert_btc_to_cur(pozadovano_v_btc, zadana_mena)

print("Pro nákup " +str(pozadovano_v_btc) + " " + prevodnik.get_symbol() +" je potřeba " + str(cena) + " "+ zadana_mena)