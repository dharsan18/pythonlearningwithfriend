from random import random


def number_to_text(number: int) -> str :
    if number == 0 : 
        return 'rock'
    elif number == 1 :
        return 'paper'
    elif number == 2 :
        return 'scissor'
    else :
        return 'invalid input'
    
def game() :
    entered_value = int(input('Please enter 0 for rock, 1 for paper and 2 for scissor\n'))
    random_value = random()
    if random_value >0 and random_value < .33 :
        computer_value = 0
    elif random_value >= .33 and random_value <.66 :
        computer_value = 1
    else :
        computer_value = 2
    if entered_value == computer_value : 
        print("Both you and computer choosen {}".format( number_to_text(computer_value)))
    elif entered_value == 0 and computer_value != 1 :
        print ("You own! Computer picked {}".format(number_to_text(computer_value)))
    elif entered_value == 0 and computer_value == 1 :
        print ("You lost! Computer picked {}".format(number_to_text(computer_value)))
    elif entered_value == 1 and computer_value != 2 :
        print ("You own! Computer picked {}".format(number_to_text(computer_value)))
    elif entered_value == 1 and computer_value == 2 :
        print ("You lost! Computer picked {}".format(number_to_text(computer_value)))
    elif entered_value == 2 and computer_value == 1:
        print ("You own! Computer picked {}".format(number_to_text(computer_value)))
    elif entered_value == 2 and computer_value != 1:
        print ("You lost! Computer picked {}".format(number_to_text(computer_value)))
    game()

if __name__ == "__main__":
    print("Welcome to the rock,paper,scissor game")
    game()
    