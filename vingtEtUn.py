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
    lines = [
        "",
        "The goal of the game is to score 21 points, or as near as possible without going over.",
        "The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.",
        "",
        "  • A player who totals over 21 is bust and loses the game",
        "  • The player whose total is nearest 21, after each player has had a turn, wins the game.",
        "  • In the case of an equality high total, the game is tied.",
        "",
        "The game is over at the end of a round when:",
        "  • One or both players are bust.",
        "  • Both players choose to stay.",
        "",
        "Notes",
        "  • Once a player totals 14 or more, one of the dies is discarder for the consecutive turns.",
        "  • The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.",
        ""
    ]
    rules = "\n".join(lines)
    print(rules)
    return

def playGame():
    ...


def takeTurn(turn: int, player: str = "house") -> dict:
    ...


def main() -> None:

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
------------------------------------------------------------------------------------
"""
    print(banner)
    USERNAME = input("Enter player name: ").strip() # Get the user's name
    print(f"\nHello {USERNAME}!\n") # Greet the user

    while True:
            print("Choose from the following options:")
            print("  1. View the Rules.\n  2. Play Vingt-et-un.\n  3. Quit.\n") # Display menu options
            user_input = input("Select an option (1|2|3): ").strip() # Get the player's choice
            # Check to make sure the user entered a digit. This eliminates the need to set up a try-except block to catch the ValueError caused by subsequently converting the input to an integer.
            if user_input.isdigit(): 
                choice = int(user_input)
                if choice > 0 and choice <= 3:
                    if choice == 1:
                        showRules()
                    elif choice == 2:
                        playGame()
                    elif choice == 3:
                        sys.exit()          
                else:
                    print(f"Error ... {choice} is not an integer in the range 1 - 3\n")
            else:
                print(f"Error ... Invalid option. Please enter 1, 2, or 3\n")
    return


if __name__ == "__main__":
    main()