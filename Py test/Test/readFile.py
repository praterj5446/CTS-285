#
#
#
#
def display_menu():
    print("Menu")
    print("")
    print("1. Requirements for memBank.csv to work or be read from.")
    print("2. Display the equations.")
    print("3. Exit.")
        
def main():
    again = "y"
    num1 = []
    num2 = []
    #numOfNum = 0
    answer = ''
    guess = int()
    while again.lower() == "y" or again.lower()== "yes":
        display_menu()
        option = int(input("Please enter your choice: "))
        print("")

        if option == 1:
            print("Open memBank.csv and make sure equations are")
            print('like "1,+,2" with nothing else on the same row.')
#            numOfNum = int(input("How many numbers do you want to enter? "))
#            number_file = open('memBank.csv', 'w')
#            for count in range(1, numOfNum +1):
#                print("Enter an equation. Equation", count, ": ")
#                numEntry = input()
#                number_file.write(str(numEntry) + '\n')
#            number_file.close()
            
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
                            print(firstNum, sign, secondNum, "=???")
                            guess = int(input())
                        if guess == answer:
                            print("Correct")
                    elif sign == "-":
                        answer = int(num1) - int(num2)
                        while guess != answer:
                            print(firstNum, sign, secondNum, "=???")
                            guess = int(input())
                        if guess == answer:
                            print("Correct")
                    elif sign == "*":
                        answer = int(num1) * int(num2)
                        while guess != answer:
                            print(firstNum, sign, secondNum, "=???")
                            guess = int(input())
                        if guess == answer:
                            print("Correct")
                    elif sign == "/":
                        answer = int(num1) / int(num2)
                        while guess != answer:
                            print(firstNum, sign, secondNum, "=???")
                            guess = int(input())
                        if guess == answer:
                            print("Correct")
                    else:
                        print("Error")
#                    print(firstNum, sign, secondNum)
#                    print("'input answer' would go here")
                    
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
            print("")
        
main()
