#First script created for the purpose of not me needing to be moving the mouse whilst being online on microsfot teams
#duration is for how many seconds it takes to get from point A to point B
#sleep is for how long the mouse will stay idle
#it is crucial to download mouse in to the computer to use this script.
#cmd -> pip3 install mouse

import mouse
import time

while (True) :
    mouse.move(1000,350, absolute=True, duration=1)
    time.sleep(200)
    mouse.move(1100,450, absolute=True, duration=1)
    time.sleep(200)
    
    

 