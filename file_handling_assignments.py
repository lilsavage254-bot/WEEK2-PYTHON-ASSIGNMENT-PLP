try :

    file = open("my_file.txt", "w")
    my_file = file.writelines(["I am a student at Egerton University School", "\nof Science and Technology", "\npursuing a degree in Computer Science", "\nYear 1", "\nSemester 1"])
    file.close()

    file = open("my_file.txt", "r")
    print(file.read())
    file.close()

    file = open("my_file.txt", "a")
    file.writelines(["\nI like coding", "\nI am a programmer", "\nI am a software developer", "\nI am a web developer"])
    file.close()

except FileNotFoundError as e:
    print(f"File not found: {e}")

except PermissionError as e:
    print(f"Permission denied: {e}")

finally :
    print("File created successfully")




