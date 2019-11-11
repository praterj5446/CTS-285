import NumberGuesser as numGuess
import AnswerChecker as calc
import memoryBank as memory

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
            memory.memBank()
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 - 3.')

main()
