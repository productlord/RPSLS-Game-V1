#part of a homework assignment I completed during my Computing Foundations Certificate Course at Rice University

import math
import random

# Assign "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


def name_to_number(name):
   
    if name == "rock":
        conversion = 0
    elif name == "Spock":
        conversion = 1
    elif name == "paper":
        conversion = 2
    elif name == "lizard":
        conversion = 3
    elif name == "scissors":
        conversion = 4
    else:
        print "Error: Choose one of rock, paper, scissors, lizard, Spock"
    return conversion
        

def number_to_name(number):
  
    if number == 0:
        conversion = "rock"
    elif number == 1:
        conversion = "Spock"
    elif number == 2:
        conversion = "paper"
    elif number == 3:
        conversion = "lizard"
    elif number == 4:
        conversion = "scissors"
    else:
        print "Error: valid numbers are 0,1,2,3,4"
    return conversion
    
      

def rpsls(player_choice): 
           
    # printing a blank line to separate consecutive game tries
    print

    # announcing the player's choice
    print "Player chooses "+ player_choice

    # converting the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # computing random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses "+ comp_choice

    # compute difference of comp_number and player_number modulo five
    mod5diff = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if mod5diff == 0:
        print "Player and computer tie!"
    elif mod5diff == 1 or mod5diff == 2:
        print "Computer wins!"
    elif mod5diff == 3 or mod5diff == 4:
        print "Player wins!" 
    else:
        print "Game Error"
        
#calling various inputs to see who wins the game - player or computer 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

#working on version 2 where I will take player_choice inputs via the browser

