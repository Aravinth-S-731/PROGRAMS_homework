import random                               #inbuilt random function
dice_lim = 6                                #total number of faces/numbers in a dice
dice_numbers = [1,2,3,4,5,6]                #numbers in dice
p1_points , p2_points = 0 , 0               #intial points of two players
p1_row,p1_col,p2_row,p2_col = -1,-1,-1,-1   #players1 position and players2 position
p1__row_temp , p1__col_temp = -1 , -1       #temporary variable to store postion of player1
p2__row_temp , p2__col_temp = -1 , -1       #temporary variable to store postion of player2
option = "y"                                #whether players want to continue

def ask_user_to_roll():                     #function to ask user to roll the dice
    global option,p1_row,p1_col,p2_row,p2_col   #global variables
    print("ROLLING DICE FOR BOTH PLAYERS")      
    dice_number_genarater()                     #calling the function to genarate dice numbers
    print("Player 1 : Row :",p1_row,"Column :",p1_col)  #player1 postion(dice numbers)
    print("Player 2 : Row :",p2_row,"Column :",p2_col)  #player2 postion(dice numbers)
    print_board_pattern()                       #calling funtion to print the board pattern
    check_for_point()                           #calling funtion to check for points
    option = input("ROLL NEXT (y/n) : ")        #whether user want to continue

def dice_number_genarater():                #funtion to genarate random dice number
    global p1_row,p1_col,p2_row,p2_col      #global variables
    p1_row = random.choice(dice_numbers)    #genrate random dice number for player1 ROW
    p1_col = random.choice(dice_numbers)    #genrate random dice number for player1 COL
    p2_row = random.choice(dice_numbers)    #genrate random dice number for player2 ROW
    p2_col = random.choice(dice_numbers)    #genrate random dice number for player2 COL

def check_for_point():                      #funtion to check points
    global p1_points,p2_points,p1_row,p1_col,p2_row,p2_col  #global varables
    global p1__row_temp , p1__col_temp,p2__row_temp , p2__col_temp  #global variables
    p1_check_row , p1_check_col = p2_row - p1__row_temp, p2_col - p1__col_temp  #differce between the previous roll of player1 and current roll of player2
    p2_check_row , p2_check_col = p1_row - p2__row_temp, p1_col - p2__col_temp  #differce between the previous roll of player2 and current roll of player1
    if (p1_row == p2__row_temp) and (p1_col == p2__col_temp):   #if player1 stands 0n player2 position
        p1_points += 1                                          #player1 gets point
    if (p2_row == p1__row_temp) and (p2_col == p1__col_temp):   #if player2 stands on player1 position
        p2_points += 1                                          #player2 gets point
    #player2 stands in postion with distace 1-space player1 gets a point
    if ((p1_check_row  == 0) or (p1_check_row  == 1) or (p1_check_row  == -1)) and ((p1_check_col  == 0) or (p1_check_col  == 1) or (p1_check_col  == -1)):
        p1_points += 1  #player1 gets point
    #player1 stands in postion with distace 1-space player2 gets a point
    if ((p2_check_row  == 0) or (p2_check_row  == 1) or (p2_check_row  == -1)) and ((p2_check_col  == 0) or (p2_check_col  == 1) or (p2_check_col  == -1)):
        p2_points += 1  #player2 gets point
    p1__row_temp , p1__col_temp = p1_row , p1_col   #assigning the postion to temporary_variable
    p2__row_temp , p2__col_temp = p2_row , p2_col   #assigning the postion to temporary_variable
    print("POINTS :\tP1 = ",p1_points,"\tP2 = ",p2_points)

def print_board_pattern():                  #funtion to print the board pattern with players position
    for index1 in range(dice_lim):          #first for loop for printing the ROW
        for index2 in range(dice_lim):      #second for loop for printing the COLUMN
            if (p1_row-1 == index1) and (p1_col-1 == index2):   #if position is same as player1 position
                print(" 1",end=" ")         #print "1" at the position
                continue                
            if (p2_row-1 == index1) and (p2_col-1 == index2):   #if position is same as player2 position
                print(" 2",end=" ")         #print "2" at the position
                continue
            #if neither of the above condition is true
            if (p1_row-1 != index1) or (p1_col-1 != index2) or (p2_row-1 != index1) or (p2_col-1 != index2):
                print(" *",end=" ")         #print "*" at empty space
        print("\n")                         #print new line
    return index1,index2

def check_result():                         #funtion to check result
    while ((p1_points or p2_points) < 5) and (option == "y"):   #while user want to continue and points in below 5
        ask_user_to_roll()                  #calling the function to roll the dice 
    if (p1_points >= 5) or (p1_points > p2_points): #if player1 scored 5 points or greater than player2
        print("\n\t-----------------------")
        print("\tPLAYER 1 WON! Congrats ")  
    elif(p2_points >= 5) or (p2_points > p1_points):#if player2 scored 5 points or greater than player1
        print("\n-----------------------")
        print("\tPLAYER 2 WON! Congrats ")
    else:                                           #else the game draws
        print("\n-----------------------")
        print("GAME DRAW!")
    print("\tPOINTS SCORED : PLAYER 1: ",p1_points," PLAYER 2:",p2_points)


print("STARTING THE GAME...")
check_result()                              #calling the funtion to check result

"""
-------------------- OUTPUT --------------------
STARTING THE GAME...
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 3 Column : 3
Player 2 : Row : 1 Column : 4
 *  *  *  2  *  *

 *  *  *  *  *  *

 *  *  1  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  0         P2 =  0
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 4 Column : 2
Player 2 : Row : 6 Column : 1
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  1  *  *  *  * 

 *  *  *  *  *  *

 2  *  *  *  *  *

POINTS :        P1 =  0         P2 =  0
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 1 Column : 3
Player 2 : Row : 3 Column : 3
 *  *  1  *  *  *

 *  *  *  *  *  *

 *  *  2  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  * 

POINTS :        P1 =  1         P2 =  0
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 4 Column : 4
Player 2 : Row : 6 Column : 4
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  1  *  *

 *  *  *  *  *  * 

 *  *  *  2  *  *

POINTS :        P1 =  1         P2 =  1
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 6 Column : 4
Player 2 : Row : 4 Column : 5
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  2  *

 *  *  *  *  *  *

 *  *  *  1  *  *

POINTS :        P1 =  3         P2 =  2
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 6 Column : 5
Player 2 : Row : 4 Column : 5
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  2  *

 *  *  *  *  *  *

 *  *  *  *  1  *

POINTS :        P1 =  3         P2 =  2
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 4 Column : 5
Player 2 : Row : 6 Column : 1
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  1  * 

 *  *  *  *  *  *

 2  *  *  *  *  *

POINTS :        P1 =  4         P2 =  3
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 3 Column : 2
Player 2 : Row : 1 Column : 3
 *  *  2  *  *  *

 *  *  *  *  *  *

 *  1  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  3
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 1 Column : 4
Player 2 : Row : 1 Column : 5
 *  *  *  1  2  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 2 Column : 1
Player 2 : Row : 5 Column : 2
 *  *  *  *  *  *

 1  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  2  *  *  *  * 

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 3 Column : 2
Player 2 : Row : 4 Column : 5
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  1  *  *  *  *

 *  *  *  *  2  *

 *  *  *  *  *  *

 *  *  *  *  *  * 

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 2 Column : 6
Player 2 : Row : 6 Column : 2
 *  *  *  *  *  *

 *  *  *  *  *  1

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  2  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 4 Column : 1
Player 2 : Row : 2 Column : 1
 *  *  *  *  *  *

 2  *  *  *  *  *

 *  *  *  *  *  *

 1  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 2 Column : 5
Player 2 : Row : 6 Column : 5
 *  *  *  *  *  *

 *  *  *  *  1  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  2  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 1 Column : 1
Player 2 : Row : 1 Column : 3
 1  *  2  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 4 Column : 6
Player 2 : Row : 2 Column : 3
 *  *  *  *  *  *

 *  *  2  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  1

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 2 Column : 5
Player 2 : Row : 1 Column : 3
 *  *  2  *  *  *

 *  *  *  *  1  *

 *  *  *  *  *  *

 *  *  *  *  *  * 

 *  *  *  *  *  *

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 5 Column : 6
Player 2 : Row : 3 Column : 2
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  2  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  1

 *  *  *  *  *  *

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 5 Column : 1
Player 2 : Row : 6 Column : 2
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 1  *  *  *  *  *

 *  2  *  *  *  * 

POINTS :        P1 =  4         P2 =  4
ROLL NEXT (y/n) : y
ROLLING DICE FOR BOTH PLAYERS
Player 1 : Row : 5 Column : 6
Player 2 : Row : 4 Column : 1
 *  *  *  *  *  *

 *  *  *  *  *  *

 *  *  *  *  *  *

 2  *  *  *  *  *

 *  *  *  *  *  1

 *  *  *  *  *  *

POINTS :        P1 =  5         P2 =  4
ROLL NEXT (y/n) : y

        -----------------------
        PLAYER 1 WON! Congrats
        POINTS SCORED : PLAYER 1:  5  PLAYER 2: 4
"""