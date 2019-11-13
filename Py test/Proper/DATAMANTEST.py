import AnswerChecker as calc
import NumberGuesser as numGuess
import memoryBank as memory
import readFile as readFile

def main():
    menu()   

def menu():
    keep_going = 'y'
    while (keep_going=='y'):
        print("Menu")
        print("1. Calculator")
        print("2. Number Guesser")
        print("3. Pop Quiz")
        print("4. Read File")
        print("5. Exit")
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            calc.ACmenu()
        elif choice == 2:
            numGuess.game()
        elif choice == 3:
            memory.memBank()
        elif choice == 4:
            readFile.read()
        elif choice == 5:
            print("Exiting")
            keep_going = 'n'
        else:
            print('\nChoice was not valid.  Please choose a valid option between 1 - 3.')
        
if __name__=="__main__":
    main()