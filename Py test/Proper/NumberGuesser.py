#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:23:28 2019

@author: daniel
"""
import random
def main():
    game()
    
def game():
    hiddenNum = int()
    guess = int()
    again = "yes"
    yesOrNo = ''
    list = []
    length = int()
    
    while again.lower() == "yes" or again.lower() == "y":
        hiddenNum = random.randint(1,1000)
        print("Guess The Number Between 1 And 1000")
        print("With The Fewest Guesses!")
        print("If you want to end early type 0.")
        while hiddenNum != guess:
            try:
                guess = int(input("Enter a number: "))
                if guess == 0:
                    print("Exiting, the correct number was", hiddenNum)
                    guess = hiddenNum
                elif guess > hiddenNum:
                    print("Too high. Try again.")
                elif guess < hiddenNum:
                    print("Too low. Try again.")
                else:
                    print("Congratulations. You guessed the number!",\
                          hiddenNum)
                list.append(guess)
            except:
                print("Please only integers!")
        print(list)
        length = len(list)
        if length < 11:
            print("Either you know the secret or you got lucky!")
        elif length >= 11:
            print("You should be able to do better!")
        yesOrNo = input('Do you want to play again? ("Y/N"): ')
        
        while yesOrNo.lower() != "yes" and yesOrNo.lower() != "no" and \
        yesOrNo.lower() != "y" and yesOrNo.lower() != "n":
            yesOrNo = input('Do you want to play again? ("Y/N"): ')
        if yesOrNo.lower() == "no" or yesOrNo.lower() == "n":
            again = "no"
            print("")
        list.clear()

if __name__=="__main__":
    main()
