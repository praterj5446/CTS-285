import NumberGuesser as numGuess
import AnswerChecker as calc

def main():
    menu()   
    
def menu():
    keep_going = 'y'
    while (keep_going=='y'):
        print("Menu")
        print("1. Calculator")
        print("2. Number Guesser")
        print("3. Memory Bank")
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            calc.ACmenu()
        elif choice == 2:
            numGuess.game()
        elif choice == 3:
            print("Sorry but the Memory Bank currently can not be loaded")
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 - 3.')

main()
