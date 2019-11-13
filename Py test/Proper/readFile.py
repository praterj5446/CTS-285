#
#
#
#
def main():
    read()

def display_menu():
    print("Menu")
    print("")
    print("1. Requirements for memBank.csv to work or be read from.")
    print("2. Display the equations.")
    print("3. Exit.")
        
def read():
    again = "y"
    num1 = []
    num2 = []
    answer = ''
    guess = int()
    while again.lower() == "y" or again.lower()== "yes":
        try:
            display_menu()
            option = int(input("Please enter your choice: "))
            print("")
    
            if option == 1:
                print("Open memBank.csv and make sure equations are")
                print('like "1,+,2" with nothing else on the same row.')                
            elif option == 2:
                try:
                    infile = open('ReadFromHere.csv', 'r')
                    for line in infile:
                        firstNum, sign, secondNum = line.split(',')
                        firstNum = firstNum.strip('"')
                        firstNum = firstNum.strip()
                        sign = sign.strip()
                        secondNum = secondNum.strip()
                        
                        
                        num1 = firstNum[0]
                        num2 = secondNum[0]
                        
                        
                        if sign == "+":
                            answer = int(num1) + int(num2)
                            while guess != answer:
                                print("Incorrect")
                                print("")
                                print(firstNum, sign, secondNum, "=???")
                                guess = int(input())
                            if guess == answer:
                                print("Correct")
                        elif sign == "-":
                            answer = int(num1) - int(num2)
                            while guess != answer:
                                print("Incorrect")
                                print("")
                                print(firstNum, sign, secondNum, "=???")
                                guess = int(input())
                            if guess == answer:
                                print("Correct")
                        elif sign == "*":
                            answer = int(num1) * int(num2)
                            while guess != answer:
                                print("Incorrect")
                                print("")
                                print(firstNum, sign, secondNum, "=???")
                                guess = int(input())
                            if guess == answer:
                                print("Correct")
                        elif sign == "/":
                            answer = int(num1) / int(num2)
                            while guess != answer:
                                print("Incorrect")
                                print("")
                                print(firstNum, sign, secondNum, "=???")
                                guess = int(input())
                            if guess == answer:
                                print("Correct")
                        else:
                            print("Error")                       
                except:
                    print("An error occurred trying to read the file")
                    print("Make sure that memBank.csv exists, that")
                    print("equations are correctly formatted, and that")
                    print("your input is valid.")
                infile.close
            elif option == 3:
                print("Exiting.")
                again = "n"
            else:
                print("Please enter one of the three options.")
        except:
            print("")
            print("Please enter a number, and one of the options")

if __name__=="__main__":
    main()