#Samantha Shoecraft tcss 142A Professor Charles Bryan.

import random

#Precondtions: none
#Postcondintions: runs program again
def main():
    
    #call program again
    again()
    
#Preconditions: Called in main function to start game
#Postconditons: Will run game and ask user if wants to repeat
#This function asks for user input, controls the turns, and asks if the players would
#like to repeat the game.
def again():
    user = "YES"
    #While loop to keep game going for as long as players would like
    
    while user.upper() == "YES" or user.upper() == "Y":
        
        #Get player input
        player1 = input("Player1, please enter your name, or enter computer to play computer: ")
        player2 = input("Player2, please enter your name, or enter computer to play computer: ")
        
        #Call function to get list to make random board
        board = game_board()
        
        #Insert 0 into index 0 to make referencing piles easier
        board.insert(0,0)
        
        #Call funtion that prints board
        print_board(board)
        
        #Make wile loop with nested if statement to make turns only go when there
        #Are stones left in the board
        while sum(board) != 0:
            board = turn(board, player1)
            if sum(board) != 0:
                board = turn (board, player2)
                
        #Ask user if they would like to coninue
        user = input("Would you like to play agian? Enter Y or Yes to play again,\
anything else to quit: ")

#Preconditions: none
#Postconditions: Return list of 2 to 5 in length of numbers 1 to 8
#This function creates the random list used for the game board
def game_board():
    board = [random.randrange(1,8) for i in range(random.randint(2,5))]
    return board

#Preconditions: List of randomly generated numbers
#Postconditions: Prints board for nim game
#This fuction is to print the game board for every turn in each game
def print_board(lst):
    print ("Let's look at the board now.")
    print ("---------------------------")
    #pPint piles with "O" representing each stone in pile
    for item in range(1,len(lst)):
        print("Pile {}:    {}".format(item, "O"*lst[item]))
    print ("---------------------------")

#Preconditon:takes in board list and player name who's turn it is
#Postcondition: returns new board list
#Will have  player remove stones from piles and make sure moves are
#   valid. Will run program with strategy. Will return new board list for next players
#   turn.
def turn(lst, player):
    board = lst
    #Call strategy function
    x, stones, pile = strategery(board)

    #prints strategy
    print("Hint: nim sum is {}." .format(x))
    print("Take {} stones out of Pile {}".format(stones, pile))   
    pilenum = len(board)-1
    answer = False
    #checks to see if player is computer
    if player.lower() == 'computer':
        board[pile] -= stones
    #Create while loop to make sure that person is making valid integer choices
    else:
        while answer == False:
            stones = input("{} please input the number of stones you wish to remove: ".format(player))
            pile = input("Pick a pile to remove from: ")
            if stones.isdigit() and pile.isdigit():
                stones = int(stones)
                pile = int(pile)
                if stones <= 0 or pile <= 0 or pile > pilenum :
                    print("Hmmm. You entered an invalid value, try again {}.".format(player))
                elif stones > board[pile] :
                    print("Hmmm. You entered an invalid value, try again {}.".format(player))
                 
                else:
                    #When player makes a valid choice, remove stones from pile mentioned
                    answer = True
                    board[pile] = board[pile] - stones
                
            else:
                print("Hmmm. You entered an invalid value, try again {}.".format(player))
    #print board
    print_board(board)
    #check for more stones. if no declaire winner
    if sum(board) == 0:
        print("{} is the winner of this round!".format(player))

    #Return new list for next players turn
    return board

#Preconditions: Takes in board list
#Postconditions: prints nim sum and suggested move
#  This function takes in the board list and will make a suggested move based on the nim
#   score. If the score is 0, it will suggest you take all the stones out of the last pile
def strategery(lst):
    board = lst
    pile = 0
    stones = 0
    x= 0
    num_pile = num_piles(board)
    boardord = board[:]
    boardord.sort()
    #Gets nim sum for board
    for i in range(len(board)):
        x= board[i] ^ x

    #Checks if sum is equal to 0, suggests all in last pile with stones    
    if x == 0:
        for i in range(len(board)-1, -1,-1) :
            if board[i] > 0:
                pile = i
                stones = board[i]
                break
    #checks to see if 2 piles left to give better guess
    elif num_pile == 2:
        x = boardord[-2]
        stones = boardord[-1] - boardord[-2]
        pile = board.index(boardord[-1])
        
    else:
        #Checks to see if x is greater than largest pile, recalculates nim score without largest number.
        #Removes new nim score from largest pile amount to get number of stones for suggested.
        if x > boardord[-1]:
            x = 0
            for i in range((len(boardord)-1)):
                x = x^boardord[i]
            stones = boardord[-1] - x
            pile = board.index(boardord[-1])
            
        #Suggest removing biggest pile if nim is equal to biggest pile    
        elif x == boardord[-1]:
            stones = boardord[-1]
            pile = board.index(boardord[-1])

        #Suggests removing nim score from largest pile.    
        else:
            
            if x in board:
                pile = board.index(x)
                stones = x
            else:
                stones = x
                pile = board.index(boardord[-1])
    return (x,stones,pile)

#Preconditions: takes in board data
#Postconditions: returns number of piles with stones
#Funtction will be used to tell how many piles on the board still have stones
def num_piles (board):
    total= 0
    for i in board:
        if i > 0:
            total +=1
    return total
        
main()
