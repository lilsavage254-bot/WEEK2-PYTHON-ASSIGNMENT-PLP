def calculate_discount(price, discount_percent) :
    if(discount_percent >= 20) :
        result = price - ((20/100) * price)
        return result
    else :
        return price 
    
original_price = int(input("Enter the original price : "))
discount_percentege = int(input("Enter the discount percentage : "))

print(calculate_discount(original_price, discount_percentege))