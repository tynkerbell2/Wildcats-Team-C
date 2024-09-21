# ------------------------------------------
# 
# 	Project:      Coriolanus Snow
#	Author:       Schilliam
#	Created:      9/21/24
#   Last Updated: 9/21/24
#	Description:  Coriolanus Snow's Code
# 
# ------------------------------------------

# Library imports
from vex import *\

# Begin project code
brain.screen.set_pen_width(100)

brain.screen.print("                       Hello")
brain.screen.next_row()
brain.screen.print("                       I am ")
brain.screen.next_row()
brain.screen.next_row()
brain.screen.next_row()
brain.screen.next_row()
brain.screen.print("                   Cornyolanus Snow")

controller_1.screen.print("    Welcome User")
controller_1.rumble(".................-.")

Intake.set_velocity(100,PERCENT)

def take_in():
    Intake.spin(REVERSE)
    Track.spin(REVERSE)

taking_in = False;

while (True):
    if(!taking_in):
        controller_1.buttonR2.pressed(take_in)
    else:
        controller_1.buttonR2.pressed(motor_lock)
    
if 

def motor_lock():
    Intake.stop()


