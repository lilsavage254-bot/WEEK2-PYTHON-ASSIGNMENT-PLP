import urllib.request, urllib.parse, urllib.error
import json
import time

url = "https://v6.exchangerate-api.com/v6/a5ed20c81e633d4a55ca72d5/latest/USD"

source = urllib.request.urlopen(url).read()

print("Enter amount to be converted.....")
amount = float(input('>'))
print("Enter the currency you want to convert....")
target_currency = input('>')
print("Converting USD to", target_currency.upper())

def currency_converter():
    
    data = json.loads(source)


    with open('CURRENCY/currency.json', 'w') as f:
            json.dump(data, f, indent=2)
            
    dict = {}
    for currency in data['conversion_rates']:
            dict[currency] = data['conversion_rates'][currency]


    try:
        print(f"1 USD is equal to {dict[target_currency.upper()]} {target_currency.upper()}")
        print(f"The amount you entered is equal to {amount * dict[target_currency.upper()]} {target_currency.upper()}")
    except KeyError:
        print("Please enter a valid currency")
        exit()

if __name__ == '__main__':
      while True:
        currency_converter()
        print("Do you want to convert another currency?(yes/no)")
        response = input('>')
        if response != 'yes':
            time_wait = 10
            print(f'Waiting {time_wait} minutes...')
            time.sleep(time_wait * 60)
        else:
             break

        
        