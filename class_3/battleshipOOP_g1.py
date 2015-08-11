from random import shuffle

class battleship(object):
    
    def __init__(self):
        self.board = gameboard()
        self.begin()
        #self.board.display()
        
    def begin(self):
        print "Welcome to BATTLESHIP"
        gamemode = 1;
        gamemode = raw_input("Choose OFFENSE OR DEFENSE or quit(O|D|q):")
        while gamemode:
            if gamemode     == "O":
                self.offense()
                break
            elif gamemode   == "D":
                self.defense()
                break
            elif gamemode   == "q":
                break
            else: 
                print "Invalid gamemode chosen: {0}".format(gamemode)
                gamemode = raw_input("Please choose OFFENSE OR DEFENSE or quit(O|D|q):")
                
    def defense(self):
        self.board.display()
        self.prompt_ship_placement()
        self.generate_offense()
    
    #utility functions for defense
    def prompt_ship_placement(self):
        while self.board.shipcount != 0:
            print       "Of your remaining ships:"
            print       "key\tship\t\tsize\tnumber"
            print       "___\t____\t\t____\t______"
            for ship in self.board.shipdict.keys():
                print   "{0}\t{1}\t{2}\t{3}".format(ship,
                                                    self.board.shipname[ship], 
                                                    self.board.shipsize[ship], 
                                                    self.board.shipdict[ship])
            ship            = raw_input("Choose a ship to place [a|p|s]:")
            while ship not in ["a","p","s"]: 
                ship        = raw_input("Invalid ship key! Please type [a|p|s]:")
                
            if self.board.shipdict[ship] != 0:
                self.board.shipdict[ship] -= 1
                align       = raw_input("Choose an alignment [h|v]")
                while align not in ["h","v"]: 
                    align   = raw_input("Invalid alignment! Please type [h|v]")
                    
                print   "Choose a row and column for ship placement (top of ship if vertical, left of ship if horizontal):"
                move        = False
                while move  == False:
                    try:
                        print   "Invalid ship placement!"
                        row     = raw_input("Choose a row letter A-J (capital letter):")
                        col     = int(raw_input("Choose a column number:"))
                        move    = self.board.check_ship_placement(  row, 
                                                                    col, 
                                                                    align, 
                                                                    ship)
                    except ValueError:
                        move = False
                        print   "Invalid ship placement!"
                        print   "Choose a row and column for ship placement (top of ship if vertical, left of ship if horizontal):"

                self.board.update(move[0],move[1],ship) 
                self.board.shipcount -= 1
                self.board.display()
            else: print "You have none of those ships remaining!"
            
        print "ship placement complete!"
    
    
    def generate_offense(self):
        hit_count       = 0
        target_count    = 0
        deck            = range(0,99)
        shuffle(deck)
        for i in range(100):
            #i = deck.pop()
            row     = i%10
            col     = (i-row)/10
            target  = self.board.board[row][col]
            target_count+=1
            if hit_count != 12:
                if target !=0:
                    self.board.display()
                    if target !='X':
                        self.board.update([row],[col],'X')
                        self.board.display()
                        print "Hit at {0}{1}".format(self.board.a_j[row], col)
                        honest = raw_input("Is this true? [t|f]")
                        if honest:
                            print "You are honorable! The barrage continues!"
                        else: 
                            "Either you are lying or our calculations are incorrect! Cease Fire!"
                            break
                        hit_count+=1
            else: 
                break
        print "Game Over! It took {0} targets to sink your ships".format(target_count)
                    
            
    
    def prompt_hitmiss(self):
        pass
    
    
    def offense(self):
        pass
    

    
class gameboard(object):
    
    def __init__(self):
        #initializes:
            #empty board: list of 10 lists of size 10 filled with 0
                #key for gameboard tiles:
                    #0 = empty ocean
                    #s = submarine
                    #a = aircraft
                    #p = patrol
                    #X = a hit 
            #A-J letter keys for converting user input
            #shipdict, shipcount for keeping track of remaining ships
            #shipsize for referencing ship sizes
            #shipname for referencing ship full names
        self.board      = [[0 for col in range(10)] for row in range(10)]
        self.a_j        = ['A','B','C','D','E','F','G','H','I','J']
        self.shipdict   = {"s":1,"a":1,"p":2}
        self.shipcount  = 4
        self.shipsize  = {"s":3,"a":5,"p":2}
        self.shipname  = {"s":"Submarine","a":"Aircraft","p":"Patrol  "}
        
        
    def display(self):
        #displays current state of gameboard
        print "_",
        for col_num in range(10): 
            print col_num,
            
        print
        for row in range(10):
            print self.a_j[row],
            for col in range(10):
                print self.board[row][col],
                
            print
            
        print
    
    def update(self, rows, cols, update_char):
        #changes current character at position row,col to update_char
        for row in rows:
            for col in cols:
                self.board[row][col] = update_char
    
    def display_shiplist(self):
        #displays list of ships left to deploy
        print "Ships left to deploy:"
        print self.shipdict
    
    def check_ship_placement(self, row_letter, col_number, alignment, ship_type):
        #for vertically aligned ship
        if alignment == "v":
            #check section of column with a length equal to size of ship
            top     = self.a_j.index(row_letter)
            bottom  = top+self.shipsize[ship_type]
            rows    = range(top,bottom)
            for row in rows:
                try:
                    if self.board[row][col_number] !=0:
                        return False
                except IndexError:
                    print "Invalid {0} placement at {1}{2}".format(self.shipname[ship_type],self.a_j[row-1],col_number)
                    return False 
                    
            return [rows, [col_number]]
            
        #for a horizontally aligned ship
        elif alignment == "h":
            #check section of row with a length equal to size of ship
            left    = col_number
            right   = col_number+self.shipsize[ship_type]
            cols    = range(left,right)
            for col in cols:
                try:
                    if self.board[self.a_j.index(row_letter)][col] !=0:
                        return False
                except IndexError:
                    print "Invalid {0} placement at {1}{2}".format(self.shipname[ship_type],row_letter,col-1)
                    return False
                    
            return [[self.a_j.index(row_letter)], cols]
        


#Tests
game = battleship()