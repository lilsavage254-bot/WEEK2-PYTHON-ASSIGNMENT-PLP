name = input("Enter your name: ")

if len(name) < 3 :
    print("Name must be atleast 3 characters long")
elif len(name) >50 :
    print("Name can be a maximum of 50 characters long")
else :
    print("Name looks good!")