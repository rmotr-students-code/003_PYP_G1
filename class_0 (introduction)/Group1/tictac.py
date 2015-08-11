#tic tac toe: Summary: !!CHECKBOARD INCOMPLETE!! !!TESTS INCOMPLETE!!
#game loop:
    #update and display board
    #prompt player for move
    #check for win, if no win, restart loop



#game loop: COMPLETE
def tictactoe():
    #dictionary for moves
    move_dict = {'a1':' ','b1':' ','c1':' ',
                 'a2':' ','b2':' ','c2':' ',
                 'a3':' ','b3':' ','c3':' '}
    
    #win check
    winner = False
    print "Welcome to Group 1 Amazing Tick Tack Toe\n"
    print "This Is A Two Player Game"
    #display board
    printboard(move_dict)
    while winner != True:
        #prompt player 1; update move_dict
        move_dict[player1move()] = 'X'
        #check for win
        winner = checkboard(move_dict)
        #display board
        printboard(move_dict)
        if winner == True:
           break
        #prompt player 2
        move_dict[player2move()] = 'O'
        #check for win
        winner = checkboard(move_dict)
        #display board
        printboard(move_dict)
    print "GAME OVER"
    
#print board to reflect data: COMPLETE
def printboard(move_dict):
    print "   A B C"
    print "1 |{A1}|{B1}|{C1}| ".format(A1=move_dict['a1'],B1=move_dict['b1'],C1=move_dict['c1'])
    print "2 |{A2}|{B2}|{C2}| ".format(A2=move_dict['a2'],B2=move_dict['b2'],C2=move_dict['c2'])
    print "3 |{A3}|{B3}|{C3}| ".format(A3=move_dict['a3'],B3=move_dict['b3'],C3=move_dict['c3'])
    
#prompt player1: COMPLETE           
def player1move():           
    p1m = raw_input("Player one please enter your move with the row and column (example a1 or b3 or c4 :  ")
    return p1m

#prompt player 2: COMPLETE    
def player2move():           
    p2m = raw_input("Player twp please enter your move with the row and column (example a1 :  ")
    return p2m
    
#check board for winning combination: !!!INCOMPLETE!!!
    #still required:    check for diagonal win
                        #catch dictionary insertion errors, ie: no existing key, or invalid move
def checkboard(move_dict):
    
    #check a given row or column on the board for a winner
    def checkstraight(list_to_check):
        if all([x == 'X' for x in list_to_check]):
            print 'X wins!'
            return True
        elif all([x == 'O' for x in list_to_check]):
            print 'O wins!'
            return True
        else: return False
    #check diagonals on the board for a winner
    def checkdiagonal(list_to_check):
        pass
    
    #storage for rows and columns on board        
    row_list= []
    col_list = []
    
    #for all rows on the board, 
    for row in range(1,4):
        for col in (['a','b','c']):
            #get the value at each index in the row (' ','X', or 'O')
            row_list.append(move_dict["{c}{r}".format(c=col,r=row)])
        #check each row for all X's or all O's
        #print "winner row{0} {1}".format(row,checkstraight(row_list))
        if checkstraight(row_list):
            return True
        #clear row_list so we can store the next row to check
        row_list=[]   
    
    #for all columns on the board,
    for col in (['a','b','c']):
        for row in range(1,4):
            #get the value at each index in the col (' ','X', or 'O')
            col_list.append(move_dict["{c}{r}".format(c=col,r=row)])
        #check each column for all X's or all O's
        #print "winner col{0} {1}".format(col,checkstraight(col_list))
        if checkstraight(col_list):
            return True
        #clear col_list so we can store the next row to check    
        col_list=[]

#test definitions            
def test_tictactoe():
    tictactoe()

def test_printboard(): 
    move_dict = {'a1':' ','b1':' ','c1':' ',
                 'a2':' ','b2':' ','c2':' ',
                 'a3':' ','b3':' ','c3':' '}  
    printboard(move_dict)


#test executions
#test_printboard()
test_tictactoe()  
