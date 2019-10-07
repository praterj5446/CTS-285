import random

def main():
    menu()
    Addition()
    Subtraction()
    Devision()
    Multipilcation()
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
            Devision()
        elif choice == 4:
            Multipilcation()
        elif choice == 5:
            print('Choice was 5.  Exiting program')
            break
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 - 5.')
                
def Addition():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    userAnswer = int(input("Enter the answer you got: "))
    
    computerAnswer = number1 + number2
    print(number1, "+", number2, "=", computerAnswer)
    choice = int(input('Would you like to 1: Repeat or 2: Go to main menu: '))
    if userAnswer == computerAnswer:
        print("Congradulations!")
    else:
        print("Sorry your answer is incorrect. Please try again!")
    if choice == 1:
        pass
    elif choice == 2:
        keep_going = 'n'
    else:
        print('\nChoice was not valid.  Please choose a valid option between 1 or 2.')
def Subtraction():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    userAnswer = int(input("Enter the answer you got: "))
    
    computerAnswer = number1 - number2 
    if userAnswer == computerAnswer:
        print("Congradulations!")
    else:
        print("Sorry your answer is incorrect. Please try again!")
    
def Devision():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    userAnswer = int(input("Enter the answer you got: "))
    
    computerAnswer = number1 / number2 
    if userAnswer == computerAnswer:
        print("Congradulations!")
    else:
        print("Sorry your answer is incorrect. Please try again!")
    
def Multipilcation():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    userAnswer = int(input("Enter the answer you got: "))
    
    computerAnswer = number1 * number2 
    if userAnswer == computerAnswer:
        print("Congradulations!")
    else:
        print("Sorry your answer is incorrect. Please try again!")

main()
