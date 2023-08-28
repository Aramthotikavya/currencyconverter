# Pre-defined exchange rates (as of the knowledge cutoff date)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.49,
    'GBP': 0.72,
    'CAD': 1.26,
    # Add more exchange rates as needed
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported."

    conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * conversion_rate
    return converted_amount

# User input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency (e.g., USD): ").upper()
to_currency = input("Enter the target currency (e.g., EUR): ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)

if isinstance(converted_amount, str):
    print(converted_amount)
else:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
