# Created by Mahros




from src import currency_converter as cc

def main():
  conv = cc.CurrencyConverter()
  conv.getCurrencies()

  while True:
    if conv._currencies == None:
      print("Sorry! Service is not aviable now.")
      conv.getCurrencies()
      continue
      
    from_currency = input("Convert from? ").strip().upper()
    if from_currency not in conv._currencies:
      print("Invalid Currency! Try agin.")
      continue

    to_currency = input("Convert to? ").strip().upper()
    if to_currency not in conv._currencies:
      print("Invalid Currency! Try agin.")
      continue

    amount = float(input("What is amount? "))

    result = conv.convert(from_currency, amount, to_currency)

    if result.success:
      print(f"Convert({amount}, base={from_currency}, to={to_currency}, result={result.data})")
    else:
      print(result.msg)
      try_agin = input("Try again? ").strip().lower()

      if try_agin in ["n", "no", "nay"]:
        exit(0)
    
  

  



# run
if __name__ == "__main__":
  main()
