# Library imports
from vex import *\

# Begin project code
brain.screen.set_pen_width(100)

# Disply screen
brain.screen.print("                       Hello")
brain.screen.next_row()
brain.screen.print("                       I am ")
brain.screen.next_row()
brain.screen.next_row()
brain.screen.next_row()
brain.screen.next_row()
brain.screen.print("                   Cornyolanus Snow")

controller_1.screen.print("    Welcome User")
#controller_1.rumble(".................-.")

# setting constants
Intake.set_velocity(100,PERCENT)
taking_in = False;

# takes in the rings
def take_in():
    Intake.spin(REVERSE)
    Track.spin(REVERSE)

# stops taking in the rings
def motor_lock():
    Intake.set_stopping(HOLD)

# input loop
while (True):
    if(taking_in):
        controller_1.buttonR2.pressed(take_in)
    else:
        controller_1.buttonR2.pressed(motor_lock)
    


