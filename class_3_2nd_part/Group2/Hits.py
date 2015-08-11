from random import choice

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

ship_dict = {
'A1': 'SU', 'B1': '  ', 'C1': '  ', 'D1': '  ', 'E1': '  ', 'F1': '  ', 
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

class Game(object):
    '''Masterclass for game engine'''
    def __init__(self):
        pass
    
    
    def hit_detection(self, attack):
        print "Attacking " + str(attack)
        if ship_dict[attack] == '  ':
            print "Miss!"
            moves_dict[attack] = 'OO'
        elif ship_dict[attack] == 'SU':
            print "Submarine hit!"
            moves_dict[attack] = 'XX'
            s.hits += 1
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
            print "error catching else, check hit_detection"

class Ship(object):
    ''' Masterclass for any ship '''
    ships = ['submarine','aircraft','patrolboat1','patrolboat2']
    def __init__(self, name, hp, hits, is_sunk):
        self.name = name
        self.hp = hp
        self.hits = hits
        self.is_sunk = is_sunk
        


class Submarine(Ship):
    ''' Submarine subclass '''
    def __init__(self):
        self.name = "Submarine"
        self.hp = 3
        self.hits = 0
        self.is_sunk = False

'''
def comp_fire():
    attack = choice(moves_dict.keys()) 
    if attack in moves_dict:
        value = moves_dict[attack]
        if value != '??':
            comp_fire()
        elif value == '??':
            sleep(0.5)
            Ship.hit_detection(attack)
'''

attack = 'A1'

# this is the game loop
#Start game (create instance of game)
game1 = Game()

#create instance of ships
s = Submarine()

#choose O or D

#check values before
print s.name
print s.hits

#attack coordinate chosen

#run hit detection
game1.hit_detection(attack)

#determine outcome
print s.hits

#Run that