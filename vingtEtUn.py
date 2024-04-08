# 
# Name: 'vingtEtUn.py'
# 
# Author: Erik Solis
# 
# Date Created: Sun Mar 17 01:25:17 EDT 2024
# 
# Last Modified: Mon Apr 8 15:49:01 EDT 2024
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


def throwDice(dice_count: int) -> int:
    '''
    Function that allows the user or house to roll their die
    '''
    return sum(random.randint(1,6) for i in range(dice_count))


def playGame():

    user_total = 0
    house_total = 0

    while True:
        # The user takes their turn
        print("Rolling dice ...")
        if user_total < 14:
            user_total += throwDice(2)
        else:
            user_total += throwDice(1)
        print(f"Your Total: {user_total}\n")

        if user_total > 21:
            status = "bust"
            print(f"You {status}, House wins.\n")
            return "house"
        elif user_total == 21:
            status = "win"
            print(f"You {status}!\n")
            return "user"
        
        # The house takes it's turn
        print("Rolling dice ...")
        if house_total < 17:
            if house_total < 14:
                house_total += throwDice(2)
            else:
                house_total += throwDice(1)
            print(f"House total: {house_total}\n")
        else:
            print("House stays.\n")
        
        if house_total > 21:
            print("House busts ... you win!\n")
            return "user"
        elif house_total >= 17:
            if user_total > house_total:
                print("You win!\n")
                return "user"
            elif user_total < house_total:
                print("You lose!\n")
                return "house"
            else:
                print(f"It's a tie!\n")
                return "tie"    


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
                        victor = playGame()
                        print(f"{victor.title()} wins this round!")
                    elif choice == 3:
                        print("Goodbye ...")
                        sys.exit()          
                else:
                    print(f"Error ... {choice} is not an integer in the range 1 - 3\n")
            else:
                print(f"Error ... Invalid option. Please enter 1, 2, or 3\n")
    return


if __name__ == "__main__":
    main()