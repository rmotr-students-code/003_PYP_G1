#check board for winning combination
def checkboard(move_dict):
    
    #check a given row or column on the board for a winner
    def checkstraight(list_to_check):
        if all([x == 'X' for x in list_to_check]):
            return 'X'
        elif all([x == 'O' for x in list_to_check]):
            return 'O'
            
    #check diagonals on the board for a winner
            
    #storage for rows and columns on board        
    row_list= []
    col_list = []
    
    #for all rows on the board, 
    for row in range(1,4):
        for col in (['a','b','c']):
            #get the value at each index in the row (' ','X', or 'O')
            row_list.append(move_dict["{c}{r}".format(c=col,r=row)])
        #check each row for all X's or all O's
        print "winner row{0} {1}".format(row,checkstraight(row_list))
        #clear row_list so we can store the next row to check
        row_list=[]   
    
    #for all columns on the board,
    for col in (['a','b','c']):
        for row in range(1,4):
            #get the value at each index in the col (' ','X', or 'O')
            col_list.append(move_dict["{c}{r}".format(c=col,r=row)])
            #check each column for all X's or all O's
        print "winner col{0} {1}".format(col,checkstraight(col_list))
        #clear col_list so we can store the next row to check    
        col_list=[]


def test_checkboard():
    print "test case 1: X wins in first row"
    move_dict_case_X_row1 = {'a1':'X','b1':'X','c1':'X',
                            'a2':' ','b2':' ','c2':' ',
                            'a3':' ','b3':' ','c3':' '} 
    checkboard(move_dict_case_X_row1)
    print " "
    print "test case 2: O wins in a column"
    move_dict_case_O_col1 = {'a1':'O','b1':' ','c1':' ',
                            'a2':'O','b2':' ','c2':' ',
                            'a3':'O','b3':' ','c3':' '} 
    checkboard(move_dict_case_O_col1)
test_checkboard()