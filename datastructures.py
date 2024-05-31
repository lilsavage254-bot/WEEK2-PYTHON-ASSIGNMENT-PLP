languages = ["HTML", "CSS", "C++", "PYTHON", "JAVASCRIPT"]

#Prints languages from index 0 to end.

print(languages[0:])

#Prints all languages in the list.

print(languages[:])

#Prints languages from index 2 to 3.

print(languages[2:4])

ages = [10 , 20 , 30 , 40 , 50] 

#Prints ages before append.

print("Ages before apend : "  + str(ages))

#Appends 60 to list.

ages.append(60)

#Prints ages after append.

print("Ages after append :" + str(ages))

prime_numbers = [2 , 3, 5]

#Prints the list of prime numbers only.

print("List1 : " +str(prime_numbers))

even_numbers = [2 , 4 , 6 ,8]

#Prints the list of even numbers only.

print("List2 : " + str(even_numbers))

#Appends the list of evev numbers to the list of prime numbers.

prime_numbers.extend (even_numbers)

#Prints the appended list.

print("Appended list : " + str(prime_numbers))

subjects = ["ENGLISH", "KISWAHILI", "BIOLOGY", "CHEMISTRY", "HISTORY", "GEOGRAPHY", "RELIGION"]

#Deletes the subject at index 2 from the list.

del subjects [2]

#Prints the subjects after deleting the subject at index 2.

print(subjects)

#Deletes the subjects at index 0 to 2 from the new list.

del subjects [0:3]

#Prints the subjects after deleting subjects from index 0 to 2.

print(subjects)

#Adds the subject French to the new list.

subjects.append("FRENCH")

#Prints the subjects after adding French to the list.

print(subjects)

#Removes the subject French from the list.

subjects.remove ("FRENCH")

#Prints the subjects from the list after removing French.

print(subjects)

#Inserts French to the given index.

subjects.insert(2, "FRENCH")

#Prints the subjects after insertion of french.

print(subjects)

#Counts the number of times FRENCH is repeated in the string.

print(subjects.count("FRENCH"))

#Prints the index of French in the list.

print(subjects.index("FRENCH"))

#Prints the word that begins with highest letter in alphabetic order.

print("Maximum in subjects is: " + max(subjects))

#Prints the word that begins with the lowest letter in alphabetic order.

print("Minimum in sujects is : " +min(subjects))

#Iterating through a list and printing individual items in the list.

for item in subjects :

    print(item)

#List compreesion with each item being increased by power o 2.
    
numbers = [number*number for number in range(1 , 6) ]

print(numbers)

numbers_list = int(input("Enter a number: "))

numbers_list = [numbers_list*x for x in range(1 , 6)]

print(numbers_list)

#Printing the largest number in a list.

digits = [3, 6, 2, 8, 10]

max = digits[0]

#Usi9ng a for loop.

for digit in digits :
    if digit > max :
        max = digit 
print("Largest digit : " + str(max))


#SETS

digits = {0 , 1 , 2 , 3 , 4}

#Adds 5 to the set.

digits.add(5)

print(digits)

companies = {"Google", "Facebook", "Microsoft", "Apple"}

tech_companies = ["Lacoste", "Samsung", "Realme"]

#Updates the set with the list of tech companies.

companies.update(tech_companies)

print(companies)

#Removes the company Lacoste from the set.

companies.discard("Lacoste")

print(companies)

#UNION OF SETS

A = {1 , 2 , 3 , 4}
B = {5 , 6 , 7 , 8}

#Prints the union of sets A and B.

print("The union of sets A and B using | is : " +str(A|B))

#Prints the union of sets A and B.

print("The union of sets A and B using union() is : " +str(A.union(B)))

#INTERSECTION OF SETS.

A = {1 , 2 , 3 , 4}
B = {3 , 4 , 5 , 6}

#Prints the intersection of sets A and B.

print("The intersection of sets A and B usin & is : " +str(A & B))

#Prints the intersection of sets A and B.

print("The intersection of sets A and B using intersection() is : " +str(A.intersection(B)))

#DIFFERENCE OF SETS.

A = {1 , 2 , 3 , 4}
B = {3 , 4 , 5 , 6}

#Prints the difference of sets A and B.

print("The difference of sets A and B using - is : " +str(A - B))

#Prints the difference of sets A and B.

print("The difference of sets A and B using difference() is : " +str(A.difference(B)))

#SYMMETRIC DIFFERENCE OF SETS.

A = {1 , 2 , 3 , 4}
B = {3 , 4, 5 , 6}

#Prints the symmetric difference of sets A and B.

print("The symmetric difference of sets A and B using ^ is : " +str(A ^ B))

#Prints the symmetric differnce of sets A and B.

print("The symmetric difference of sets A and B using symmetric_difference() is : " +str(A.symmetric_difference(B)))