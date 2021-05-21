
# list [0,0,1] 
# tell it to pick a random choice on the list if it equal 
# create a a number to count the times that this happend
# take away one of the 0 from the list. 
# 1 then add that to the list of times that happenen
# loops 1000 times
# then use that number / 1000


import random
from typing import final
switch_choice = False

Win = 0
for _ in range (0,1000):

    car_position = random.randrange(3)
    first_choice = random.randrange(3)
    #print('car position: ' + str(car_position))
    #print('first choice: ' + str(first_choice))
    # if first_choice = 1 then eliminate a 0 at random. 
    # if not then elimiate the only remaining 0
    #if doors[first_choice] == 1:

    door_position = {0,1,2}
    open_door = -1
    if first_choice == car_position:
        Goat_doors = door_position.difference({car_position})
        open_door = random.choice(list(Goat_doors))
        #print('correct choice!')
    else:
        Position_of_picked_door = {car_position, first_choice}
        Whats_left = door_position.difference(Position_of_picked_door)
        open_door = Whats_left.pop()
        #print('wrong choice!')
    #print('opening door: ' + str(open_door))

    final_choice = -1
    if switch_choice == True:
        final_choice = door_position.difference({first_choice,open_door}).pop()
    else:
        final_choice = first_choice
    #print('final choice: ' + str(final_choice))


    if final_choice == car_position:
        Win = Win + 1

print (Win/1000)
