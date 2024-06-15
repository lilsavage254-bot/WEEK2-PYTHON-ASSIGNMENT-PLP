     #FOR LOOP

welcome_message = "WELCOME TO PLP"

for i in range(5) :
    print(welcome_message)


names = ["HASHIM", "BAYA", "NASSORO", "ZAKIA", "KAHASO", "YUSRA", "MARURA"]

for name in names :
    print(name)



       #WHILE LOOP
    
count = 0 
while count <= 5 :
    print(count)
    count += 1

        #BREAK STATEMENTS
    
colors = ["RED", "BLUE", "ORANGE", "WHITE", "YELLOW", "MAROON"]

for color in colors :
    print(color)

    if color == "WHITE" :
        print("They have the color I want")
        break


colors = ["RED", "BLUE", "ORANGE", "WHITE", "YELLOW", "MAROON"]

length = len(colors)
count = 0

while count < length :
    print(colors[count])

    if colors[count] == "WHITE" :
        print("They have the color I want")
        break
    count +=1

        #CONTINUE STATEMENTS

ages = [13, 24, 17, 36, 19, 27, 30]

for age in ages :

    if age < 21 :
        continue
    print(age)

#ages = [13, 24, 17, 36, 19, 27, 30]

#length = len(ages)
count = 0

#while count < length :
#    if count < 21 :
#       continue
#    count += 1
#    print(ages)

      #NESTED LOOPS

groups = [["HASHIM", "BAYA"], ["ZAKIA", "KAHASO"]]

for group in groups :
    for name in group :
        print(name)


