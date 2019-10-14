''' Jacob White
    CTS-285
    MemoryBank
    10/14/2019'''

import random
def main():
    input()       
    display()

def input():
    total = 0
    global correct
    global incorrect
    for x in range(1,10):
        
        rn = (random.randint(1,10))
        rn2 = (random.randint(1,10))
        computerResult = rn + rn2
        print(rn, ('+'), rn2)
        input1 = int(input('Enter the answer: '))
        if input1 == computerResult:
            print('Correct')
            ans1 = ('Correct')
            correct++
            global ans1                
        elif input1 != computerResult:
            print('EEEEE')
            ans1 = ('EEEEE')
            incorrect++
            global ans1
        total += input1

def display():
    print('Total Correct', correct, 'Total Incorrect', incorrect)

if __name__=="__main__":
    main()
