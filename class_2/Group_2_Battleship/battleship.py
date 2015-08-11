#This battleship program will be broken into several functions that will provide for a awesome gaming experience.

# Imports
from random import choice
from time import sleep

# Globals
style = 'O'
subhit = 0
carhit = 0 
pb1hit = 0
pb2hit = 0 
ships = ['submarine','aircraft','patrolboat1','patrolboat2']
shipmovelist=[]
subsunk = False
carsunk = False
pb1sunk = False
pb2sunk = False

def print_game_board():
    print '      A    B    C    D    E    F    G    H    I    J' 
    print '1   | ' + moves_dict['A1']+ ' | ' + moves_dict['B1']+ ' | ' + moves_dict['C1']+ ' | ' + moves_dict['D1']+ ' | ' + moves_dict['E1']+ ' | ' + moves_dict['F1']+ ' | ' + moves_dict['G1']+ ' | ' + moves_dict['H1']+ ' | ' + moves_dict['I1']+ ' | ' + moves_dict['J1']+ ' | '  
    print '2   | ' + moves_dict['A2']+ ' | ' + moves_dict['B2']+ ' | ' + moves_dict['C2']+ ' | ' + moves_dict['D2']+ ' | ' + moves_dict['E2']+ ' | ' + moves_dict['F2']+ ' | ' + moves_dict['G2']+ ' | ' + moves_dict['H2']+ ' | ' + moves_dict['I2']+ ' | ' + moves_dict['J2']+ ' | ' 
    print '3   | ' + moves_dict['A3']+ ' | ' + moves_dict['B3']+ ' | ' + moves_dict['C3']+ ' | ' + moves_dict['D3']+ ' | ' + moves_dict['E3']+ ' | ' + moves_dict['F3']+ ' | ' + moves_dict['G3']+ ' | ' + moves_dict['H3']+ ' | ' + moves_dict['I3']+ ' | ' + moves_dict['J3']+ ' | ' 
    print '4   | ' + moves_dict['A4']+ ' | ' + moves_dict['B4']+ ' | ' + moves_dict['C4']+ ' | ' + moves_dict['D4']+ ' | ' + moves_dict['E4']+ ' | ' + moves_dict['F4']+ ' | ' + moves_dict['G4']+ ' | ' + moves_dict['H4']+ ' | ' + moves_dict['I4']+ ' | ' + moves_dict['J4']+ ' | ' 
    print '5   | ' + moves_dict['A5']+ ' | ' + moves_dict['B5']+ ' | ' + moves_dict['C5']+ ' | ' + moves_dict['D5']+ ' | ' + moves_dict['E5']+ ' | ' + moves_dict['F5']+ ' | ' + moves_dict['G5']+ ' | ' + moves_dict['H5']+ ' | ' + moves_dict['I5']+ ' | ' + moves_dict['J5']+ ' | ' 
    print '6   | ' + moves_dict['A6']+ ' | ' + moves_dict['B6']+ ' | ' + moves_dict['C6']+ ' | ' + moves_dict['D6']+ ' | ' + moves_dict['E6']+ ' | ' + moves_dict['F6']+ ' | ' + moves_dict['G6']+ ' | ' + moves_dict['H6']+ ' | ' + moves_dict['I6']+ ' | ' + moves_dict['J6']+ ' | ' 
    print '7   | ' + moves_dict['A7']+ ' | ' + moves_dict['B7']+ ' | ' + moves_dict['C7']+ ' | ' + moves_dict['D7']+ ' | ' + moves_dict['E7']+ ' | ' + moves_dict['F7']+ ' | ' + moves_dict['G7']+ ' | ' + moves_dict['H7']+ ' | ' + moves_dict['I7']+ ' | ' + moves_dict['J7']+ ' | ' 
    print '8   | ' + moves_dict['A8']+ ' | ' + moves_dict['B8']+ ' | ' + moves_dict['C8']+ ' | ' + moves_dict['D8']+ ' | ' + moves_dict['E8']+ ' | ' + moves_dict['F8']+ ' | ' + moves_dict['G8']+ ' | ' + moves_dict['H8']+ ' | ' + moves_dict['I8']+ ' | ' + moves_dict['J8']+ ' | ' 
    print '9   | ' + moves_dict['A9']+ ' | ' + moves_dict['B9']+ ' | ' + moves_dict['C9']+ ' | ' + moves_dict['D9']+ ' | ' + moves_dict['E9']+ ' | ' + moves_dict['F9']+ ' | ' + moves_dict['G9']+ ' | ' + moves_dict['H9']+ ' | ' + moves_dict['I9']+ ' | ' + moves_dict['J9']+ ' | ' 
    print '10  | ' + moves_dict['A10']+ ' | ' + moves_dict['B10']+ ' | ' + moves_dict['C10']+ ' | ' + moves_dict['D10']+ ' | ' + moves_dict['E10']+ ' | ' + moves_dict['F10']+ ' | ' + moves_dict['G10']+ ' | ' + moves_dict['H10']+ ' | ' + moves_dict['I10']+ ' | ' + moves_dict['J10']+ ' | '

#Dictionaries

#Placement dictionary - Values: SU, CA, P1, P2 
ship_dict = {
'A1': '  ', 'B1': '  ', 'C1': '  ', 'D1': '  ', 'E1': '  ', 'F1': '  ', 
'G1': '  ', 'H1': '  ', 'I1': '  ', 'J1': '  ', 'A2': '  ', 'B2': '  ', 
'C2': '  ', 'D2': '  ', 'E2': '  ', 'F2': '  ', 'G2': '  ', 'H2': '  ', 
'I2': '  ', 'J2': '  ', 'A3': '  ', 'B3': '  ', 'C3': '  ', 'D3': '  ', 
'E3': '  ', 'F3': '  ', 'G3': '  ', 'H3': '  ', 'I3': '  ', 'J3': '  ', 
'A4': '  ', 'B4': '  ', 'C4': '  ', 'D4': '  ', 'E4': '  ', 'F4': '  ', 
'G4': '  ', 'H4': '  ', 'I4': '  ', 'J4': '  ', 'A5': '  ', 'B5': '  ', 
'C5': '  ', 'D5': '  ', 'E5': '  ', 'F5': '  ', 'G5': '  ', 'H5': '  ', 
'I5': '  ', 'J5': '  ', 'A6': '  ', 'B6': '  ', 'C6': '  ', 'D6': '  ', 
'E6': '  ', 'F6': '  ', 'G6': '  ', 'H6': '  ', 'I6': '  ', 'J6': '  ', 
'A7': '  ', 'B7': '  ', 'C7': '  ', 'D7': '  ', 'E7': '  ', 'F7': '  ', 
'G7': '  ', 'H7': '  ', 'I7': '  ', 'J7': '  ', 'A8': '  ', 'B8': '  ', 
'C8': '  ', 'D8': '  ', 'E8': '  ', 'F8': '  ', 'G8': '  ', 'H8': '  ', 
'I8': '  ', 'J8': '  ', 'A9': '  ', 'B9': '  ', 'C9': '  ', 'D9': '  ', 
'E9': '  ', 'F9': '  ', 'G9': '  ', 'H9': '  ', 'I9': '  ', 'J9': '  ', 
'A10': '  ', 'B10': '  ', 'C10': '  ', 'D10': '  ', 'E10': '  ', 
'F10': '  ', 'G10': '  ', 'H10': '  ', 'I10': '  ', 'J10': '  '  }

#Moves dictionary - values: ??, OO, XX 
moves_dict = {
'A1': '??', 'B1': '??', 'C1': '??', 'D1': '??', 'E1': '??', 'F1': '??', 
'G1': '??', 'H1': '??', 'I1': '??', 'J1': '??', 'A2': '??', 'B2': '??', 
'C2': '??', 'D2': '??', 'E2': '??', 'F2': '??', 'G2': '??', 'H2': '??', 
'I2': '??', 'J2': '??', 'A3': '??', 'B3': '??', 'C3': '??', 'D3': '??', 
'E3': '??', 'F3': '??', 'G3': '??', 'H3': '??', 'I3': '??', 'J3': '??', 
'A4': '??', 'B4': '??', 'C4': '??', 'D4': '??', 'E4': '??', 'F4': '??', 
'G4': '??', 'H4': '??', 'I4': '??', 'J4': '??', 'A5': '??', 'B5': '??', 
'C5': '??', 'D5': '??', 'E5': '??', 'F5': '??', 'G5': '??', 'H5': '??', 
'I5': '??', 'J5': '??', 'A6': '??', 'B6': '??', 'C6': '??', 'D6': '??', 
'E6': '??', 'F6': '??', 'G6': '??', 'H6': '??', 'I6': '??', 'J6': '??', 
'A7': '??', 'B7': '??', 'C7': '??', 'D7': '??', 'E7': '??', 'F7': '??', 
'G7': '??', 'H7': '??', 'I7': '??', 'J7': '??', 'A8': '??', 'B8': '??', 
'C8': '??', 'D8': '??', 'E8': '??', 'F8': '??', 'G8': '??', 'H8': '??', 
'I8': '??', 'J8': '??', 'A9': '??', 'B9': '??', 'C9': '??', 'D9': '??', 
'E9': '??', 'F9': '??', 'G9': '??', 'H9': '??', 'I9': '??', 'J9': '??', 
'A10': '??', 'B10': '??', 'C10': '??', 'D10': '??', 'E10': '??', 
'F10': '??', 'G10': '??', 'H10': '??', 'I10': '??', 'J10': '??'}

#New game loop run every time a game is started.
def new_game():
    global sunk, style, subhit, carhit, pb1hit, pb2hit, subsunk, carsunk, pb1sunk, pb2sunk
    subsunk = False 
    carsunk = False
    pb1sunk = False 
    pb2sunk = False
    style = 'O'
    subhit = 0
    carhit = 0 
    pb1hit = 0
    pb2hit = 0 
    print "Welcome to BattleShip" "\n" "\n"
    print "We are playing with a 10x10 board and 4 ships: \n 1 submarine (size 3) \n 1 Aircraft carrier (size 5) \n 2 Patrol boats (size 2)"  
    print_game_board()
    style = raw_input("Please enter choose [O]ffense or [D]efense: ")
    if style == 'O':
        print "We are playing Offense"
        offense()
    elif style == 'D':
        print "We are playing Defense"
        defense()
    else: 
        print "You can only enter 'O' or 'D'"

def offense():
    print "In this mode the computer position the ships and youll have to sink all of them." 
    comp_ship_move()
    y=0
    while y < 3:
        for x in shipmovelist[y]:
            if x in shipmovelist[y+1]:
                shipmovelist[:] = []
                shipmove()
        y += 1
    update_placement_dict(shipmovelist)
    print " computer has placed his ships"
    player_fire()

def defense():
    print "In this mode you place the ships and receive attacks from the computer"
    shipmove()
    y=0
    while y < 3:
        for x in shipmovelist[y]:
            if x in shipmovelist[y+1]:
                print "You have a ship collision please enter in ship cordinates again\n\n\n"
                shipmovelist[:] = []
                shipmove()
        y+=1
    update_placement_dict(shipmovelist)
    comp_fire()

def hit_checker(attack):
    global subhit, carhit, pb1hit, pb2hit
    print "Attacking " + str(attack)
    
    if ship_dict[attack] == '  ':
        print "Miss!"
        moves_dict[attack] = 'OO'
    elif ship_dict[attack] == 'SU':
        print "Submarine hit!"
        moves_dict[attack] = 'XX'
        subhit += 1
    elif ship_dict[attack] == 'CA':
        print "Carrier hit!"
        moves_dict[attack] = 'XX'
        carhit += 1 
    elif ship_dict[attack] == 'P1':
        print "Patrol boat hit!"
        moves_dict[attack] = 'XX'
        pb1hit += 1
    elif ship_dict[attack] == 'P2':
        print "Patrol boat hit!"
        moves_dict[attack] = 'XX'
        pb2hit += 1
    else:
        print "error catching else, check hit_checker"
    print_game_board()
    sink_checker()

def sink_checker():
    global subhit, carhit, pb1hit, pb2hit, subsunk, carsunk, pb1sunk, pb2sunk
    if subsunk == False:
        if subhit >= 3:
            print "Submarine has been sunk!"
            subsunk = True
    elif carsunk == False:
        if carhit >= 5:
            print "Aircraft Carrier has been sunk!"
            carsunk = True
    if pb1sunk == False:
        if pb1hit >= 2:
            print "Patrol boat 1 has been sunk!"
            pb1sunk = True
    if pb2sunk == False:
        if pb2hit >= 2:
            print "Patrol boat 2 has been sunk!"
            pb2sunk = True
    game_over_checker()

def game_over_checker():    
    global subsunk, carsunk, pb1sunk, pb2sunk
    if subsunk and carsunk and pb1sunk and pb2sunk == True:
        game_over()
    else:
        if style == 'O':
            player_fire()
        elif style == 'D':
            comp_fire()

def movevehicle(move,direction,vehicletype):
    submarinemovelist = []
    aircraftmovelist = []
    patrolboat1movelist = []
    patrolboat2movelist = []
    submarineoutofboundsvert = ['A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    submarineoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
    patrolboatoutofboundsvert = ['A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    patrolboatoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']
    aircraftoutofboundsvert = ['A8','B8','C8','D8','E8','F8','G8','H8','I8','J8','A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    aircraftoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10']
   
    #Sanity check of input from user. If user enters letter outside range A-J or Number 1-11 it will fail.
    if int(len(move)) < 2:
        print "This is an invalid move try again"
        return False
    if ord(move[0]) < 65 or ord(move[0]) > 74 :
        print "This is an invalid move try again"
        return False
    if int(len(move)) == 2:
        if int(move[1]) < 1 or int(move[1]) > 9 :
            print "This is an invalid move try again"
            return False
    if int(len(move)) ==3:
        if int(move[1] + move[2]) < 1 or int(move[1] + move[2]) > 11 :
            print "This is an invalid move try again"
            return False
    if direction == 'vertical' or direction == 'horizontal':
        pass
    else:
        print "\n\nYou entered and invalid direction. Please Enter a valid vehicle direction.\n\n\n\n"
        return False
    if direction == 'vertical' and vehicletype == 'submarine':
            for x in submarineoutofboundsvert:
                if vehicletype == 'submarine' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,3):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'aircraft':
            for x in aircraftoutofboundsvert:
                if vehicletype == 'aircraft' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,5):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'patrolboat1':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat1' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'patrolboat2':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat2' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'horizontal' and vehicletype == 'submarine':
            for x in submarineoutofboundshori:
                if vehicletype == 'submarine' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,3):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal' and vehicletype == 'aircraft':
            for x in aircraftoutofboundshori:
                if vehicletype == 'aircraft' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,5):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal' and vehicletype == 'patrolboat1':
            for x in range(0,2):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal'and vehicletype == 'patrolboat2':
            for x in range(0,2):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    #shipmovelist.append({vehicletype:submarinemovelist})
    shipmovelist.append(submarinemovelist)
    return True
    
def shipmove():
    y = 0
    while y < 4: 
        x = False
        while x == False:
            move = raw_input("Please enter the board location you want to place your {}:  ".format(ships[y]))
            direction = raw_input("Please enter the direction you wish your vehicle to be deployed (e.g vertical or horizontal):   ")
            x = movevehicle(move,direction,ships[y])
        y+=1
    return shipmovelist
    
def update_placement_dict(shipmovelist):
    
    sub = shipmovelist[0][0:3]
    aircraft = shipmovelist[1][0:5]
    pboat1 = shipmovelist[2][0:2]
    pboat2 = shipmovelist[3][0:2]
    
    for i in sub:
        ship_dict[i] = "SU"
    for i in aircraft:
        ship_dict[i] = "CA"
    for i in pboat1:
        ship_dict[i] = "P1"
    for i in pboat2:
        ship_dict[i] = "P2"

    #if style == 'O':
        #player_fire()
    #elif style == 'D':
        #comp_fire()
    
def comp_fire():
    #Needs to be expanded so comp will target adjacent squares to a hit
    attack = choice(moves_dict.keys()) 
    if attack in moves_dict:
        value = moves_dict[attack]
        if value != '??':
            comp_fire()
        elif value == '??':
            sleep(0.5)
            hit_checker(attack)
    
def comp_move_vehicle(move,direction,vehicletype):
    submarinemovelist = []
    aircraftmovelist = []
    patrolboat1movelist = []
    patrolboat2movelist = []
    submarineoutofboundsvert = ['A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    submarineoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
    patrolboatoutofboundsvert = ['A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    patrolboatoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']
    aircraftoutofboundsvert = ['A8','B8','C8','D8','E8','F8','G8','H8','I8','J8','A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    aircraftoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10']
   
    #Sanity check of input from user. If user enters letter outside range A-J or Number 1-11 it will fail.
    if int(len(move)) < 2:
        return False
    if ord(move[0]) < 65 or ord(move[0]) > 74 :
        return False
    if int(len(move)) == 2:
        if int(move[1]) < 1 or int(move[1]) > 9 :
           return False
    if int(len(move)) ==3:
        if int(move[1] + move[2]) < 1 or int(move[1] + move[2]) > 11 :
            return False
    
    
    if direction == 'vertical' or direction == 'horizontal':
        pass
    else:
        return False
    if direction == 'vertical' and vehicletype == 'submarine':
            for x in submarineoutofboundsvert:
                if vehicletype == 'submarine' and move == x:
                    return False
            for x in range(0,3):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'aircraft':
            for x in aircraftoutofboundsvert:
                if vehicletype == 'aircraft' and move == x:
                    return False
            for x in range(0,5):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'patrolboat1':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat1' and move == x:
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical' and vehicletype == 'patrolboat2':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat2' and move == x:
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'horizontal' and vehicletype == 'submarine':
            for x in submarineoutofboundshori:
                if vehicletype == 'submarine' and move == x:
                    return False
            for x in range(0,3):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal' and vehicletype == 'aircraft':
            for x in aircraftoutofboundshori:
                if vehicletype == 'aircraft' and move == x:
                    return False
            for x in range(0,5):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal' and vehicletype == 'patrolboat1':
            for x in range(0,2):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal'and vehicletype == 'patrolboat2':
            for x in range(0,2):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    #shipmovelist.append({vehicletype:submarinemovelist})
    shipmovelist.append(submarinemovelist)
    return True
    
def comp_ship_move():
    dirs = ['vertical', 'horizontal']
    y = 0
    while y < 4: 
        x = False
        while x == False:
            move = choice(moves_dict.keys())
            direction = choice(dirs)
            x = comp_move_vehicle(move,direction,ships[y])
        y+=1
    return shipmovelist
    
def player_fire():
    attack = raw_input('Please enter a coordinate to attack. e.g. B6 > ')
    if attack in moves_dict:
        value = moves_dict[attack]
        if value != '??':
            print "You've already attacked that coordinate"
            player_fire()
        elif value == '??':
            hit_checker(attack)
    else:
        print "That coordinate you entered is out of bounds"
        print ""
        player_fire()
    
def game_over():
    print "Game over"
    
    """
    ng = raw_input("[N]ew or [q]uit?")
    ng = ng.lower()
    if ng in ('n', 'ne', 'new'):
        new_game()
    elif ng in ('q', 'qu', 'qui', 'quit'):
        quit()
    else:
        print "error cathching else in game_loop()"
    """
    
new_game()
