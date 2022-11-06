# Tic Tac Toe
# McKinley Woodin

# Define variables
numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "X"
i = 1
gameover = False

#function printBoard() prints the tic tac toe board.
def printBoard():
    print(f"{numbersList[0]}|{numbersList[1]}|{numbersList[2]}")
    print("-+-+-")
    print(f"{numbersList[3]}|{numbersList[4]}|{numbersList[5]}")
    print("-+-+-")
    print(f"{numbersList[6]}|{numbersList[7]}|{numbersList[8]}")

# function switchPlayer() switched which players turn it is
def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# function checkBox() check to see if the box has already been taken.
def checkBox(num):
    while numbersList[int(num)-1] == "X" or numbersList[int(num)-1] == "O":
        num = input("That spot has already been taken please choose another: ")
    
    return num

# Checks for the 8 different winning combos
def checkForWin():
    global gameover
    if numbersList[0] == "X" and numbersList[1] == "X" and numbersList[2] == "X" or numbersList[0] == "O" and numbersList[1] == "O" and numbersList[2] == "O":
        printBoard()
        print(f"{numbersList[0]} Wins!")
        gameover = True
    elif numbersList[3] == "X" and numbersList[4] == "X" and numbersList[5] == "X" or numbersList[3] == "O" and numbersList[4] == "O" and numbersList[5] == "O":
        printBoard()
        print(f"{numbersList[3]} Wins!")
        gameover = True
    elif numbersList[6] == "X" and numbersList[7] == "X" and numbersList[8] == "X" or numbersList[6] == "O" and numbersList[7] == "O" and numbersList[8] == "O":
        printBoard()
        print(f"{numbersList[6]} Wins!")
        gameover = True
    elif numbersList[0] == "X" and numbersList[3] == "X" and numbersList[6] == "X" or numbersList[0] == "O" and numbersList[3] == "O" and numbersList[6] == "O":
        printBoard()
        print(f"{numbersList[0]} Wins!")
        gameover = True
    elif numbersList[1] == "X" and numbersList[4] == "X" and numbersList[7] == "X" or numbersList[1] == "O" and numbersList[4] == "O" and numbersList[7] == "O":
        printBoard()
        print(f"{numbersList[1]} Wins!")
        gameover = True
    elif numbersList[2] == "X" and numbersList[5] == "X" and numbersList[8] == "X" or numbersList[2] == "O" and numbersList[5] == "O" and numbersList[8] == "O":
        printBoard()
        print(f"{numbersList[2]} Wins!")
        gameover = True
    elif numbersList[0] == "X" and numbersList[4] == "X" and numbersList[8] == "X" or numbersList[0] == "O" and numbersList[4] == "O" and numbersList[8] == "O":
        printBoard()
        print(f"{numbersList[0]} Wins!")
        gameover = True
    elif numbersList[2] == "X" and numbersList[4] == "X" and numbersList[6] == "X" or numbersList[2] == "O" and numbersList[4] == "O" and numbersList[6] == "O":
        printBoard()
        print(f"{numbersList[2]} Wins!")
        gameover = True

# function main() is the main exicution.
def main():
    
    global player
    printBoard()
    square = input(f"{player}'s turn to choose a square (1-9): ")
    square = checkBox(square)
    numbersList[int(square)-1] = player
    # print(numbersList)
    switchPlayer()

# Executes the game
while i < 10 and gameover != True:
    
    main()
    checkForWin()
    i += 1
    print()
    

