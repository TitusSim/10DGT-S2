# Area and Perimeter Loop 
# Author: Titus Sim
# Date: 15/11/2024 (Last edited)
# Version: 2


def number_check(question): # This is the fragment of code that can be used over and over again. The (question) part is a placeholder for any question needed.
    error = "Invalid number, please enter a number"
    while True: # While "number_check" is running, try:
        try: 
            answer = float(input(question)) # I used 'float' so it can only take numbers
            if answer > 0: # if the answer was larger than 0 than it is a valid answer
                return answer
            else:
                print(error) # Lower than zero say invalid 
        except ValueError:
            print(error) # Not a number say invalid



loop = "" # I used this while loop to make it so that this program can run over and over again
while loop == "": # while the variable 'loop' is empty, run this code: (I will continue to run this code until the variable 'loop' holds a value)
    width = number_check("Please give width: ") # In this case the width = number_check which is the code above 
    length = number_check("Please give length: ") # Same, uses the number_check program to see if it is a valid number 

    area = width * length # Simple math formula to solve area (using width and length as variables which we found out using number_check)
    perimeter = 2 * (width + length) # math formula to solve perimeter 

    print(f"Area: {area}") # f means format, it formats the information so it's easier on the eyes for the user
    print(f"Perimeter: {perimeter}")
    print() # this makes a gap #
    # A gap is usually nice when it comes to asking a new question.
    loop = input("Again? Press enter to run program again or press any other key to end.") # this is making 'loop' the input, if user presses enter then loop remains an empty variable and the program continues
    
print("Thanks for using my program!!") # This is to show the loop has ended.
