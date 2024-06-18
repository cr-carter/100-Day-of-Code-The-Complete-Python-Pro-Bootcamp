#This purpose of this project is to practice with using while loops, logic, and basic debugging.
#This program is specific to an exercise on Reeborg's World, and can be found at this website:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#The right_turns variable will be used to detect situations where the robot starts in a location that would lead to continuous right turns, ie a 4x4 square without any walls.
#If 4 right turns are made, then the robot will no longer make any right turns before it first performs another action.
right_turns = 0
while not at_goal():
    if wall_on_right() == False and right_turns < 4:
        turn_right()
        move()
        right_turns += 1
    elif front_is_clear() == True:
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0
