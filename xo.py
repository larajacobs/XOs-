# Define the number of rows and columns
num_rows = 3
num_columns = 3

# Initialize a 2D array (matrix) with zeros
array = [[" "] * num_columns for _ in range(num_rows)]

# Add the board to it 
def printBoard():           
    print()
    for row in array:
        for column in row:
            print("|", column, "|", end="")  # Add extra characters after each element
        print()
        
def update_array(position1, position2, player):
    global array
    
    if player == "player1":
        array[position1][position2] = "x"
    elif player == "player2":
        array[position1][position2] = "o"
    
    printBoard()
        
def switchcase(name):
    global array
    
    player = name.split(",")
    players = player[-1]
    print("players: ", players)
    position = input(player[0] + " please enter position: TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
   
    #  TL, TM, TR, ML, MM, MR, BL, BM, BR
    if  position == "TL" or position == "tl":
        if (array[0][0]== " "):
            update_array(0, 0, players)
        else:
            print("Please choose another option")
            return
        
    elif position == "TM" or position == "tm":
        if (array[0][1]== " "):
            update_array(0, 1, players)
        else:
            print("Please choose another option")
    elif position == "TR" or position == "tr":
        if (array[0][2]== " "):
            update_array(0, 2, players)
        else:
            print("Please choose another option")
            return
    elif position == "ML" or position == "ml":
        if (array[1][0]== " "):
            update_array(1, 0, players)
        else:
            print("Please choose another option")
            return
    elif position == "MM" or position == "mm":
        if (array[1][1]== " "):
            update_array(1, 1, players)
        else:
            print("Please choose another option")
            return
    elif position == "MR" or position == "mr":
        if (array[1][2]== " "):
            update_array(1, 2, players)
        else:
            print("Please choose another option")
            return
    elif position == "BL" or position == "bl":
        if (array[2][0]== " "):
            update_array(2, 0, players)
        else:
            print("Please choose another option")
            return
    elif position == "BM" or position == "bm":
        if (array[2][1]== " "):
            update_array(2, 1, players)
        else:
            print("Please choose another option")
            return
    elif position == "BR" or position == "br":
        if (array[2][2]== " "):
            update_array(2, 2, players)
        else:
            print("Please choose another option")
            return
    else:
        print("Invalid choice, please choose again")
        return

def checkwin(player):
    if player == "player1":
        # 00, 01, 02
        # 10, 11, 12
        # 20, 21, 22
        # 00, 11, 22
        # 20, 11, 02
        # 00, 10, 20
        # 10, 11, 12
        # 20, 21, 22
        
        print()       
    else:
        print()

def playGame():
    player1 = input("Please enter your name: ")
    print("Hello "+player1+", you are player 1")
    
    yes = input("Would you like to play against another player? Y or N: ")

    if (yes == "Y" or yes == "y"):
        player2 = input("Please enter name of player 2: ")
    else :
        player2 = "Computer"
        
    print()
    print("Let the games begin!!!")
    print("TL = Top left")
    print("TM = Top middle")
    print("TR = Top right")
    
    print("ML = Top left")
    print("MM = Top middle")
    print("MR = Top right")
    
    print("BL = Top left")
    print("BM = Top middle")
    print("BR = Top right")
    
    print()
    
    # Needs to alternate between player 1 and player 2
    while(True):
        player1 = player1+ ",player1"
        switchcase(player1)
        checkwin("player1")
        player2 = player2+ ",player2"
        switchcase(player2)
        checkwin("player2")
           

def main():
    
    playGame()      
    # printBoard()
    
    
    
if __name__ == "__main__":
    main()