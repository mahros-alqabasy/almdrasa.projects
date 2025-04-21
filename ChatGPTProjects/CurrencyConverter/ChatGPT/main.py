from src import currency_converter as cc

def main():
    conv = cc.CurrencyConverter()
    conv.getCurrencies()

    while True:
        if conv.currencies is None:
            print("Sorry! Service is not available now.")
            conv.getCurrencies()
            continue

        print("\n=== Currency Converter ===")
        print("1. Convert currency")
        print("2. Refresh currency list")
        print("3. Show available currencies")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            from_currency = input("Convert from? ").strip().upper()
            if from_currency not in conv.currencies:
                print("Invalid Currency!")
                show = input("Show available currencies? (y/n): ").strip().lower()
                if show == "y":
                    conv.showCurrencies()
                continue

            to_currency = input("Convert to? ").strip().upper()
            if to_currency not in conv.currencies:
                print("Invalid Currency!")
                show = input("Show available currencies? (y/n): ").strip().lower()
                if show == "y":
                    conv.showCurrencies()
                continue

            try:
                amount = float(input("What is the amount? "))
            except ValueError:
                print("Invalid number. Try again.")
                continue

            result = conv.convert(from_currency, amount, to_currency)

            if result.success:
                print(f"{amount} {from_currency} = {result.data:.2f} {to_currency}")
            else:
                print("Error:", result.msg)

        elif choice == "2":
            conv.getCurrencies()
            print("Currency list refreshed.")

        elif choice == "3":
            conv.showCurrencies()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")



if __name__ == "__main__":
  main()
