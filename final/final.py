# ----------------------------------------
# Program:   Number Guessing Game (final)
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      07/17/2026
# ----------------------------------------

import random

def show_menu():            # Displays the choices for the player
    print()
    print("NUMBER GUESSING GAME")
    print("1. Play")
    print("2. View wins and losses")
    print("3. Run tests")
    print("4. Quit")
    
def check_guess(guess, answer): # Returns whether the guess is too high, too low, or correct
    if guess < answer:
        return "low"
    elif guess > answer:
        return "high"
    else:
        return "correct"

def valid_number(number): # Returns True if the number is between 1 and 1000
    if number >= 1 and number <= 1000:
        return True
    else:
        return False
    
def read_stats():# reads the wins and losse s from the text file
    wins = 0
    losses = 0
    try:
        stats_file = open("game_stats.txt", "r")
        wins = int(stats_file.readline())
        losses = int(stats_file.readline())
        stats_file.close()
    
    except: # If the file does not exist then start at zero
        wins = 0
        losses = 0
        
    return wins, losses

def write_stats(wins, losses): # Writes the wins and losses to the text file
    stats_file = open("game_stats.txt", "w")
    stats_file.write(str(wins) + "\n")
    stats_file.write(str(losses) + "\n")
    stats_file.close()
    
def play_game():# chooses a random number from 1 up to 1000
    answer = random.randrange(1, 1001)
    tries = 0
    won = False
    
    print()
    print("I picked a number between 1 and 1000.")
    print("You have 10 tries to guess it.")
    
    while tries < 10 and won == False:
        print()
        print("Try number:", tries + 1)
        
        try:
            guess = int(input("Enter your guess: "))
            
            if valid_number(guess) == False:
                print("Enter a number between 1 and 1000.")
            else:
                tries = tries + 1
                result = check_guess(guess, answer)
                
                if result == "low":
                    print("Too low.")
                
                elif result == "high":
                    print("Too high.")
                
                else:
                    print("Correct!")
                    print("You guessed it in", tries, "tries.")
                    won = True
        except:
            print("Please enter a whole number.")
            
    if won == False:
        print()
        print("You lost.")
        print("The correct number was", answer)

    return won
def show_stats(wins, losses):# Displays the saved number of wins and losses
    print()
    print("Wins:", wins)
    print("Losses:", losses)
    
def run_tests():# Tests the fruitful functions
    print()
    print("RUNNING TESTS")
    
    if check_guess(5, 10) == "low":
        print("Test 1 passed.")
    else:
        print("Test 1 failed.")
    if check_guess(15, 10) == "high":
        print("Test 2 passed.")
    else:
        print("Test 2 failed.")
    if check_guess(10, 10) == "correct":
        print("Test 3 passed.")
    else:
        print("Test 3 failed.")
    if valid_number(500) == True:
        print("Test 4 passed.")
    else:
        print("Test 4 failed.")
    if valid_number(1001) == False:
        print("Test 5 passed.")
    else:
        print("Test 5 failed.")
        
def main():# Reads the saved statistics when the program starts
    wins, losses = read_stats()
    
    choice = ""
    

    while choice != "4":# Keeps displaying the menu until the player quits
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            won = play_game()
            
            if won == True:
                wins = wins + 1
            else:
                losses = losses + 1
            write_stats(wins, losses)
        elif choice == "2":
            show_stats(wins, losses)
        elif choice == "3":
            run_tests()
        elif choice == "4":
            print("Thanks for playing!")
        else:
            print("That is not a valid option.")
            
main()
