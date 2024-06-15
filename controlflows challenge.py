def large_power(base, exponent ) :
     if(base ** exponent > 5000 ) :
         return True
     else :
         return False 


Base = int(input("Enter a base : "))
Exponent = int(input("Enter an exponent : "))

print(large_power(Base, Exponent))

def divisible_by_ten(num) :
    if(num % 10 == 0) :
        return True 
    else :
        return False
    
num = int(input("Enter a number : "))
print(divisible_by_ten(num))