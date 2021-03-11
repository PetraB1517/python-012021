"""Fake news
Moduly v Pythonu se často snaží zpříjemnit život programátorům.
Například je občas otrava vymýšlet jména nebo adresy, když chceme vyzkoušet, jestli náš program funguje.
Jindy třeba potřebujeme nějaká data anonymizovat, tj. odebrat z nich citlivé osobní údaje jako jména, adresy atd.
Pro tento účel existuje modul Faker, která nám umí vygenerovat jména, adresy a řadu dalších dat,
které můžeme využít při testování našich programů.
"""

from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

print(generator_falesnych_dat.name())
print(generator_falesnych_dat.address())


class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address
"""    
Zkus nyní vytvořit nějaký objekt ze třídy Balik a přiřadit mu náhodně vygenerované jméno příjemce a adresu.
Pomocí funkce get_info() si nech informace o balíku vypsat.
"""
balik = Balik(generator_falesnych_dat.name(),generator_falesnych_dat.address())

balik.get_info()

"""
Pokročilejší varianta
Uvažujme nyní společnost, která přepravuje balíky do více zemí.
Zkus nyní upravit svůj program tak, aby generoval adresy v rámci České i Slovenské republiky.
Příslušnou zkratku pro Slovensko najdeš taktéž v dokumentaci k modulu."""

from faker import Faker
generator_fake_lidi = Faker(["cs_CZ", "sk_SK"])
Faker.seed(0)

balik2 = Balik(generator_fake_lidi["cs_CZ"].name(), generator_fake_lidi.address())
balik3 = Balik(generator_fake_lidi["cs_CZ"].name(), generator_fake_lidi.address())
balik4 = Balik(generator_fake_lidi["cs_CZ"].name(), generator_fake_lidi.address())

balik2.get_info()
balik3.get_info()
balik4.get_info()
