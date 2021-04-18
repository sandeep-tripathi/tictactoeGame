
#Creating the board
# Dictionary with each value as empty
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

# Empty list where values will be appended
board_keys = []

# loop through a dictionary and append it's key to  empty list at previous line
for key in theBoard:
    board_keys.append(key)    


" Function to display the board as the keyboard patterns"
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-+')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-+')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# ticTackToe() is the main function with required functionality
def ticTackToe():

# First player will be assigned 'X'
    turn = 'X'
    count = 0


    for i in range(10):  # Number range from 1 to 9
        printBoard(theBoard)  # Displays the board
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        # Taking user input

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue   # Skip the iteration of the loop

        # After each 5 moves, check if any player won ...Winning strategy
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal is not empty space i.e. filled
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'Tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Switching player after each move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Ask if player wants a new game.
    # This should not be inside the for loop 
    new_game = input("Do want to play Again? Press 'y' or 'n':")
    if new_game == "y" or new_game == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        ticTackToe()   # Recursion

if __name__ == "__main__":
   ticTackToe()






    
