from unittest import result
from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("Saississez le montant : "))
from_currency = input("De quelle devise ? ").upper()
to_currency = input("Vers quelle devise ? ").upper()

print(f"{amount} de {from_currency} vers {to_currency} : ")
result_amount = c.convert(from_currency,to_currency, amount)

print( result_amount)

