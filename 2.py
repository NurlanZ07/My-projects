import random
import sys


def main():
    energy=10
    room=1
    print('Let`s go')
    while True:
        direction=direct()
        room=current_room(room,direction)
        kind=kind_of_room(direction)
        energy=energy_change(energy,kind)

        print(f'Room = {room}\nEnergy = {energy}\nRoom Outcome = {kind}')
        if room==9:
            print('That was very close, you lost')
    
        if room==10:
            print('Congrats, you won')
            break
        
        if energy<=0:
            print('Unfortunately, you lost')
            break
    replay()
    


def direct():
    while True:
        direction=input(('In which direct do you want to move? forward,left or right?')).strip().lower()
        if direction in ['forward','right','left']:
            break
        else:
            print('Incorrect direction.')
    return direction
    
         
def current_room(room,direction):
    if direction=='forward':
        room+=1   
    return room
    

def kind_of_room(direction):
    chance=random.random()
    if direction=='forward':
        rule=0.2
        trap=trap(chance,rule)
    elif direction=='right' or direction=='left':
        rule=0.4
        trap=trap(chance,rule)
   
    if trap:
        kind='Trap room'
    else:
        kind='Safe room'
    return kind


def trap(chance,rule):
    if chance>=rule:
        trap=True
    else:
        trap=False
    return trap



def energy_change(energy,kind):
    if kind=='Safe room':
        energy-=1
    elif kind=='Trap room':
        energy-=2
    
    return energy


def replay():
    ask=input('Do you want to replay? (y/n)').strip().lower()
    if ask=='yes':
        main()
    else:
        sys.exit()
    


main()
    



    