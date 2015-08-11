#list of first 10 letters in alphabet
a_j = ['A','B','C','D','E','F','G','H','I','J']
#dict with ship char keyed to length of ship
ship_size ={"s":3,"a":5,"p":2}
ship_name ={"s":"Submarine","a":"Aircraft Carrier","p":"Patrol"}
#game loop for battleship
def battleship_gameloop(): #Complete

    #gameboard is stored as a list of 10 lists of size 10
    #key for gameboard tiles:
        #0 = empty ocean
        #s = submarine
        #a = aircraft
        #p = patrol
        #X = a hit 
    gameboard = [[0 for col in range(10)] for row in range(10)]
    shipdict = {"s":1,"a":1,"p":2}
    
    #gameloop for choosing gamemode
    print "Welcome to BATTLESHIP"
    gamemode = 1;
    while gamemode:
        gamemode = raw_input("Choose OFFENSE OR DEFENSE or quit(O|D|q):")
        if gamemode == "O":
            offense(gameboard)
        elif gamemode == "D":
            defense(gameboard)
        elif gamemode == "q":
            break
        else: 
            print "Invalid gamemode chosen: {0}".format(gamemode)
            gamemode = raw_input("Please choose OFFENSE OR DEFENSE or quit(O|D|q):")



#functions shared by both deffense and attack:
def display_board(gameboard): #Complete
    print "_",
    for col_num in range(10): print col_num,
    print
    for row in range(10):
        print a_j[row],
        for col in range(10):
            print gameboard[row][col],
        print
    print
    
def update_board(gameboard,rows,cols,update_char): #Complete
    #changes current character at position row,col to update_char
    for row in rows:
        for col in cols:
            gameboard[row][col] = update_char

def display_shiplist(shipdict): #Complete
    #displays list of ships left to deploy
    print "Ships left to deploy:"
    print shipdict

def check_ship_placement(gameboard,row_letter,col_number,alignment,ship_type,update_char): #INCOMPLETE
    gameboard_cpy = gameboard[:][:]
    #attempt to place ship
    #for a vertically aligned ship
    if alignment == "v":
        #check section of column with a length equal to size of ship
        top = a_j.index(row_letter)
        bottom = top+ship_size[ship_type]
        check_rows = range(top,bottom)
        for row in check_rows:
            try:
                if gameboard[row][col_number] !=0:
                    return False
                #else:
                    #gameboard_cpy[row][col_number]=update_char
            except IndexError:
                print "Invalid {0} placement at {1}{2}".format(ship_name[ship_type],a_j[row-1],col_number)
                return False 
        return [check_rows, [col_number]]
    #for a horizontally aligned ship
    elif alignment == "h":
        #check section of row with a length equal to size of ship
        left = col_number
        right = col_number+ship_size[ship_type]
        check_cols = range(left,right)
        for col in check_cols:
            try:
                if gameboard[a_j.index(row_letter)][col] !=0:
                    return False
                #else: 
                    #gameboard_cpy[a_j.index(row_letter)][col] = update_char
            except IndexError:
                print "Invalid {0} placement at {1}{2}".format(ship_name[ship_type],row_letter,col-1)
                return False
        return [[a_j.index(row_letter)], check_cols]
    

def check_board():
    
    pass

#defense function and utility functions used by defense():
#let's start listing out in sequential order what happens for a defensive game
def defense(gameboard): #Incomplete
    
#loop for placing ships:
    #display board
    display_board(gameboard)
    #display remaining ships
    #prompt for ship type and placement
    #check if valid shipt type and valid placement
    #update board

#loop for defense sequence:
    #display board
    #generate random attack coordinates (can use 'from random import randint')
    #prompt player to specify hit or miss
    #check for honesty
    #update board
    #check for win
    pass

#utility functions for defense
def prompt_ship_placement():
    pass


def generate_offense():
    pass

def prompt_hitmiss():
    pass

#attack function and utility functions used by attack():
def offense(gameboard):

#generate random ship placement for console
#update (hidden) board (this will be done in a loop much like that for the offensive
#version but the coordinate and ship selection will be random, and the board shall not
#be displayed ever

#loop for offense sequence:
    #prompt player for attack coordinates

    #specify hit or miss
    #update (hidden) board
    #check for win
    pass
#utility functions for attack:
def generate_ship_placement():
    pass

def prompt_offense(): #incomplete
    guess_row = int(raw_input("Guess Row"))
    guess_col = int(raw_input("Guess Col"))
    pass

def specify_hitmiss():
    pass


    
#Tests
def test_battleship_gameloop():
    battleship_gameloop()
    
def test_display_board():
    display_board([[0 for col in range(10)] for row in range(10)])

def test_check_ship_placement():
    gameboard = [[0 for col in range(10)] for row in range(10)]
    print "test: vertical aircraft carrier at A4"
    move1= check_ship_placement(gameboard,"A",4,"v","a","a")
    if move1:
        update_board(gameboard, move1[0],move1[1],"a")
        display_board(gameboard)
    print "test: horizontal aircraft carrier at J8"
    move2= check_ship_placement(gameboard,"J",8,"h","a","a")
    if move2:
        update_board(gameboard, move2[0],move2[1],"a")
        display_board(gameboard)
#test_battleship_gameloop()
test_display_board()
test_check_ship_placement()