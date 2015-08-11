###############################
# Class [Class variables]
#    Subclasses [Subclass variable]
#
# Ship [name, hp, hits, is_sunk ]
#    Submarine
#    Carrier
#    PatrolBoat1
#    PatrolBoat2
#
# GameBoard
#    PlacedBoard
#    MoveBoard
###############################

class Ship(object):
    ''' Masterclass for any ship '''
    def __init__(self, name, hp, hits, is_sunk):
        self.name = name
        self.hp = hp
        self.hits = hits
        self.is_sunk = is_sunk
        
    def hit_detection():
        pass
    
    def sink_detection():
        pass


class Sumarine(Ship):
    ''' Submarine subclass '''
    #Class Variables for lists of out of bounds movement for this class vehicle.
    submarineoutofboundsvert = ['A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    submarineoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
    
    def __init__(self, name, hp, hits, is_sunk):
        self.name = "Submarine"
        self.hp = 3
        self. hits = 0
        self.is_sunk = False

class Carrier(Ship):
    ''' Aircraft Carrier subclass '''
     #Class Variables for lists of out of bounds movement for this class vehicle
    aircraftoutofboundsvert = ['A8','B8','C8','D8','E8','F8','G8','H8','I8','J8','A9','B9','C9','D9','E9','F9','G9','H9','I9','J9','A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    aircraftoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10']
    def __init__(self, name, hp, hits, is_sunk):
        self.name = "Aircraft Carrier"
        self.hp = 5
        self. hits = 0
        self.is_sunk = False

class PatrolBoat1(Ship):
    ''' Patrolboat1 subclass '''
     #Class Variables for lists of out of bounds movement for this class vehicle
    patrolboatoutofboundsvert = ['A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    patrolboatoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']
    def __init__(self, name, hp, hits, is_sunk):
        self.name = "Patrol Boat"
        self.hp = 2
        self. hits = 0
        self.is_sunk = False

class Patrolboat2(Ship):
    ''' Patrolboat2 subclass '''
    #Class Variables for lists of out of bounds movement for this class vehicle
    patrolboatoutofboundsvert = ['A10','B10','C10','D10','E10','F10','G10','H10','I10','J10']
    patrolboatoutofboundshori = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']
    
    def __init__(self, name, hp, hits, is_sunk):
        self.name = "Patrol Boat"
        self.hp = 2
        self. hits = 0
        self.is_sunk = False
        
class valitityofmove(object):      
  
    def __init__(self,move,direction,vehicletype):
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
        
        
        
        
        
shipmovelist = []        
        
        
x = valitityofmove('A10','vertical','patrolboat1')

print shipmovelist

t = PatrolBoat1( 'PatrolBoat1', 3, 0, False)

print t.patrolboatoutofboundshori