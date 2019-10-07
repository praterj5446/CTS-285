"""Jessica Prater
08/27/2019
CTS-285
M1HW"""

def main():
    menu()
    Addition()
    Subtraction()
    Devision()
    Multiplication()
    EndProgram()
    
def menu():
    keep_going = 'y'
    while (keep_going=="y"):
        print("Menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Devision")
        print("4. Multipilcation")
        print("5. End Program")
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            Addition()
        elif choice == 2:
            Subtraction()
        elif choice == 3:
            Division()
        elif choice == 4:
            Multipilcation()
        elif choice == 5:
            print('Choice was 5.  Exiting program')
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 - 5.')
                
def Addition():
    keep_going = 'y'
    while (keep_going=="y"):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        
        computerAnswer = number1 + number2
        print(number1, "+", number2, "=", computerAnswer)
        choice = int(input('Would you like to 1: Repeat or 2: Go to main menu: '))
        if choice == 1:
            pass
        elif choice == 2:
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 or 2.')
    
def Subtraction():
    keep_going = 'y'
    while (keep_going=="y"):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        
        computerAnswer = number1 - number2
        print(number1, "-", number2, "=", computerAnswer)
        if choice == 1:
            pass
        elif choice == 2:
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 or 2.')
    
def Devision():
    keep_going = 'y'
    while (keep_going=="y"):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        
        computerAnswer = number1 / number2
        print(number1, "/", number2, "=", computerAnswer)
        if choice == 1:
            pass
        elif choice == 2:
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 or 2.')
    
def Multipilcation():
    keep_going = 'y'
    while (keep_going=="y"):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        
        computerAnswer = number1 * number2 
        print(number1, "*", number2, "=", computerAnswer)
        if choice == 1:
            pass
        elif choice == 2:
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 or 2.')

main()
