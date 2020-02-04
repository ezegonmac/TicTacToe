# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:20:19 2020

FROM 15:20 to 17:54

@author: ezquielgon2
"""
    #   GLOBAL VARIABLES
   
Board = [" "," "," ",
         " "," "," ",
         " "," "," ",]

Turn = "X"

Winner = None

Game_still_going = True

    #   FUNCTIONS

def print_board():
    '''Take a list(0-9) and print it formatted'''
    
    print(" {} | {} | {}".format(Board[0], Board[1], Board[2]))
    print("-- + - + --")
    print(" {} | {} | {}".format(Board[3], Board[4], Board[5]))
    print("-- + - + --")
    print(" {} | {} | {}".format(Board[6], Board[7], Board[8]))
    
    print("\n"*2)

def print_intro():
        
    print("======================")
    print("|  TIC - TAC - TOE   |")
    print("======================")
    print("\nThe positions will be")
    print("set with the following numbers:")
    print("-----------")
    print(" 1 | 2 | 3  \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
    print("-----------")
    print("\n"*2)
    

def ask_and_place_position():
    '''Ask for a position'''
    
    print("{}'s turn".format(Turn))
    
    index = check_if_position_is_valid()
    
    # PLACE THE GIVEN POSITION
    Board[index] = Turn
            
def check_if_position_is_valid():
    '''Check if the given position isnt used yet
       and in the range of index of the board.
       
       Also returns the index'''
    
    valid_position = False
    while valid_position == False:
        print("Choose a number from 1 to 9:")
        position = int(input())
        
        index = position - 1
        # CHECK IF POSITION IS VALID
        if index in range(9): # Check if position in range
            if Board[index] == " ": # Check if position isnt used yet
                valid_position = True
            else:
                valid_position = False
                print("The given position is used yet, try again.")
                print_board()
        else:
            valid_position = False
            print("The given position is out of range, try again.")
            print_board()
    
    return index


def flip_player():
    global Turn
    
    if Turn == "X":
        Turn = "O"
    else:
        Turn = "X"
        
        
def check_if_game_still_going():
    
    check_lines()
    check_tie()
    
    
def check_lines():
    global Winner
    
    check_rows()
    check_columns()
    check_diagonals()
    
    # PRINT MESSAGE IF LINE
    if Game_still_going == False:
        Winner = Turn
        print("LINE !")
        print("WINNER: {}".format(Winner))
        
################ CHECK LINES ####################
        
def check_rows():
    global Game_still_going
    
    if Board[0] == Board[1] == Board[2] != " ":
        Game_still_going = False
    if Board[3] == Board[4] == Board[5] != " ":
        Game_still_going = False
    if Board[6] == Board[7] == Board[8] != " ":
        Game_still_going = False
        
        
def check_columns():
    global Game_still_going
    
    if Board[0] == Board[3] == Board[6] != " ":
        Game_still_going = False
    if Board[1] == Board[4] == Board[7] != " ":
        Game_still_going = False
    if Board[2] == Board[5] == Board[8] != " ":
        Game_still_going = False
        
        
def check_diagonals():
    global Game_still_going
    
    if Board[0] == Board[4] == Board[8] != " ":
        Game_still_going = False
    if Board[2] == Board[4] == Board[6] != " ":
        Game_still_going = False
###################################################
    
def check_tie():
    global Game_still_going
    
    Game_still_going = False
    for i in Board:
        if i == " ":
            Game_still_going = True
            pass
    
    # PRINT MESSAGE IF TIE
    if Game_still_going == False:
        print("TIE !")
        print("There isn't a WINNER...")
    
def play_game():
    '''Manage the functions'''
    global Game_still_going
    global Winner
    
    print_intro()
    
    while Winner == None and Game_still_going:
        # ask for position AND place position
        ask_and_place_position()
        
        # check game 
        check_if_game_still_going()
        
        # flip player
        flip_player()
        
        # show board
        print_board()

    
    
    #----------------#
    #| MAIN PROGRAM |#
    #----------------#
    
play_game()


#--------#
# SCHEME #
#--------#

 # Board
 # print board
 # start game
 # flip player
 # ask if line
 # ask if tie
