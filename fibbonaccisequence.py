             #QUESTION 1
# Functions & Fibonacci Sequence


#generate_fibonacci_sequence function:
#This function takes an integer n as input.
#It generates a list of the first n terms of the Fibonacci sequence.

def generate_fibonacci_sequence(n):

#Initializes a list called sequence with the first two values as 0 and 1.

            
    sequence = [0, 1]

#Then , it iterates through the range from 2 to n .   
     
    for i in range(2, n):

#For each iteration, it calculates the next term in the sequence by adding the last two terms in the sequence.
                
        next_term = sequence[i-1] + sequence[i-2]

#It appends the next term to the sequence list.
                
        sequence.append(next_term)

#It returns the generated fibonacci sequence.
                
    return sequence

#Prompts user to enter the value of n which is the number of terms in the fibonacci sequence.
#It converts the user input to an integer using the int() function and assigns it to the variable n.
  
n = int(input("Enter the value of n: "))

#The generate_fibonacci_sequence function is called with the value of n obtained from the user input.
#The resulting Fibonacci sequence is stored in the variable fibonacci_sequence.

fibonacci_sequence = generate_fibonacci_sequence(n)

#The code prints the Fibonacci sequence up to the nth term.
#It uses an f-string to format the output string, including the value of n and the generated Fibonacci sequence.
#The formatted string is printed using the print() function.

print(f"Fibonacci sequence up to term {n}: {fibonacci_sequence}")