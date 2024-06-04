# Description: File handling assignments
try :   

    file = open("my_file.txt", "w")       # Open the file in write mode
        #  Write to the file
    my_file = file.writelines(["I am a student at Egerton University School", "\nof Science and Technology", "\npursuing a degree in Computer Science", "\nYear 1", "\nSemester 1"])
    file.close()                          # Close the file

    file = open("my_file.txt", "r")       # Open the file in read mode
    print(file.read())                    # Read the file and print on console.
    file.close()                          # Close the file

    file = open("my_file.txt", "a")       # Open the file in append mode
    file.writelines(["\nI like coding", "\nI am a programmer", "\nI am a software developer", "\nI am a web developer"])      # Append to the file
    file.close()                          # Close the file

except FileNotFoundError as e:            # Handle file not found error
    print(f"File not found: {e}")         

except PermissionError as e:             # Handle permission error
    print(f"Permission denied: {e}")     

finally :                                # Finally block
    print("File created successfully")




