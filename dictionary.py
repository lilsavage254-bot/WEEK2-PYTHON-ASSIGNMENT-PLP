capital_city ={
    'KENYA ': 'NAIROBI' , 
    'TANZANIA ': 'DODOMA', 
    'UGANDA ': 'KAMPALA', 
    'SOUTH AFRCA ': 'JOHANESBURG'
    }
print(capital_city.get('KENYA'))

phone = input("Phone : ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = " "
for ch in phone :
    output += digits_mapping.get(ch, "!") + " "

print(output)
