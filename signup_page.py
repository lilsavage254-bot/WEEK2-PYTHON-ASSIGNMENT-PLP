print("Create account now")
username = input("Enter username : ")
password = input("Enter password : ")

print("Account created succsesifully")
print("Login now!")

username2 = input("Enter username : ")
password2 = input("Enter password : ")

if username == username2 and password == password2 :
    print("Logged in succsessifully!")
else :
    print("Invalid username or password")
