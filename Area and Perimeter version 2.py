# Area and Perimeter Loop 
# Author: Titus Sim
# Version: 2


def number_check(question):
    error = "Invalid number, please enter a number"
    while True:
        try: 
            answer = float(input(question)) 
            if answer > 0:
                return answer
            else:
                print(error)
        except ValueError:
            print(error)



loop = ""
while loop == "":
    width = number_check("Please give width: ")
    length = number_check("Please give length: ")

    area = width * length
    perimeter = 2 * (width + length)

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print()
    loop = input("Again? Press enter to run program again or press any other key to end.")
    
print("Thanks for using my program!!")

