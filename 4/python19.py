"""Instalace modulu
Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně, ale umí si kurz měny stáhnout z internetu.
"""
from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = 10
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)
"""

Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()).
Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK.
Následně od uživatele získej i požadované množství cílové měny. Nezapomeň toho množství převést na typ int.

Pokročilejší varianta
Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí, například převod měny do Bitcoinu. Zkus pomocí modulu vytvořit program, který se zeptá uživatele na měnu a požadovaný počet Bitcoinů a vrátí mu množství měny, které by potřeboval, aby požadované množství Bitcoinů mohl koupit."""