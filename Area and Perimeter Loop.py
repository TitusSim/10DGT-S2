# 
#
#

loop = ""
while loop == "":
    try:
        width = float(input("Please enter the width: "))
        if width > 0:
            loop = 2
        else: 
            print("Please enter a number that is more than 0")
    except ValueError:
        print("Please enter a numberical value!")
        loop = ""

    
    _loop = ""
    while _loop == "":
        try: 
            height = float(input("Now enter the height: "))
            if height > 0:
                _loop = 2
            else:
                print("Please enter a number that is more than zero")
        except ValueError:
            print("Please enter a numerical value!")

    perimeter = 2 * (height + width)
    area = height * width

    print()
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")
    loop = input("Again?")


print("Thanks for using my program!")