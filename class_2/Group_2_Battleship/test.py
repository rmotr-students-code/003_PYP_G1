
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
    if direction == 'vertical':
        if vehicletype == 'submarine':
            for x in submarineoutofboundsvert:
                if vehicletype == 'submarine' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,3):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical':
        if vehicletype == 'aircraft':
            for x in aircraftoutofboundsvert:
                if vehicletype == 'aircraft' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,5):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical':
        if vehicletype == 'patrolboat1':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat1' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'vertical':
        if vehicletype == 'patrolboat2':
            for x in patrolboatoutofboundsvert:
                if vehicletype == 'patrolboat2' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,2):
                submarinemovelist.append(move[0] + str((int(move[1]))+x))
    if direction == 'horizontal':
        if vehicletype == 'submarine':
            for x in submarineoutofboundshori:
                if vehicletype == 'submarine' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,3):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal':
        if vehicletype == 'aircraft':
            for x in aircraftoutofboundshori:
                if vehicletype == 'aircraft' and move == x:
                    print "You have placed a vehicle out of bounds!!! Please re-enter moves\n\n\n"
                    return False
            for x in range(0,5):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal':
        if vehicletype == 'patrolboat1':
            for x in range(0,2):
                submarinemovelist.append(chr(ord(move[0])+x)+move[1])
    if direction == 'horizontal':
        if vehicletype == 'patrolboat2':
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


ships = ['submarine','aircraft','patrolboat1','patrolboat2']
shipmovelist=[]
print 'You have access to the following ships\n'
print 'Each of the follwing ships have a corrisponding lenght\n\n'

print shipmove()
#shipmovelist


y=0
while y < 3:
    for x in shipmovelist[y]:
        if x in shipmovelist[y+1]:
            print "You have a ship collision please enter in ship cordinates again\n\n\n"
            shipmovelist[:] = []
            shipmove()
    y+=1





