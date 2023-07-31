def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.73,
        "JPY": 110.65,
        "INR": 74.8,  # Add the exchange rate for INR (Indian Rupee)
        # Add more exchange rates as needed
    }

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency"

    # Convert amount from the 'from_currency' to USD first
    usd_amount = amount / exchange_rates[from_currency]

    # Convert from USD to the 'to_currency'
    converted_amount = usd_amount * exchange_rates[to_currency]
    return converted_amount

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP, JPY, INR): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP, JPY, INR): ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)

    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
