print('Těším se na dnešní hodinu dlouhodobého kurzu!')
"""import wget
wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
"""

"""Úvod do importů"""

from forex_python.converter import CurrencyRates
c = CurrencyRates()
print(c.get_rates('CZK'))

c = CurrencyRates()
rates = c.get_rates('CZK')
for key, value in rates.items():
  rate = 1 / value
  print(f"1 {key} = {round(rate, 2)}")

currencyList = ["GBP", "EUR", "USD"]
for key, value in rates.items():
  if key in currencyList:
    rate = 1 / value
    print(f"1 {key} = {round(rate, 2)}")



"""úvod do pandas"""
import pandas
nakupy = pandas.read_csv('nakupy.csv')
print(nakupy)
nakupy.info()

print(nakupy.shape)

print(nakupy.shape[0])

print(nakupy.columns)

print(nakupy.iloc[3])

print(nakupy.iloc[0:5])
