# 
# Name: 'vingtEtUn.py'
# 
# Author: Erik Solis
# 
# Date Created: Sun Mar 17 01:25:17 EDT 2024
# 

import sys
import random



def showRules() -> None:
    '''
    Prints the rules to the screen
    '''
    return

def playGame():
    return


def takeTurn(player: str, turn: int) -> dict:
    return


def main():

    # Program Banner
    banner = """
 __      __  _                   _                     _                            
 \ \    / / (_)                 | |                   | |                           
  \ \  / /   _   _ __     __ _  | |_   ______    ___  | |_   ______   _   _   _ __  
   \ \/ /   | | | '_ \   / _` | | __| |______|  / _ \ | __| |______| | | | | | '_ \ 
    \  /    | | | | | | | (_| | | |_           |  __/ | |_           | |_| | | | | |
     \/     |_| |_| |_|  \__, |  \__|           \___|  \__|           \__,_| |_| |_|
                          __/ |                                                     
                         |___/                    
    ----------------------------------------------------------------------------
------------------------------------------------------------------------------------\n
"""
    print(banner)
    USERNAME = input("Enter player name: ").strip() # Get the user's name
    print(f"Hello {USERNAME}!") # Greet the user

    while True:
            print("1. View the Rules.\n2. Play Vingt-et-un.\n3. Quit.") # Display menu options
            user_input = input("Choose from the  options: ").strip() # Get the player's choice
            # Check to make sure the user entered a digit. This eliminates the need to set up a try-except block to catch the ValueError caused by subsequently converting the input to an integer.
            if user_input.isdigit(): 
                choice = int(user_input)
                if choice > 0 and choice >= 3:
                    if choice == 1:
                        showRules()
                    elif choice == 2:
                        playGame()
                    elif choice:
                        sys.exit()
                    
                else:
                    print(f"Error ... {choice} is not an integer in the range 1 - 3")
            else:
                print(f"Error ... Invalid option. Please enter 1, 2, or 3")
    return


if __name__ == "__main__":
    main()