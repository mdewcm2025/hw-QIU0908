def turn_right():
    for i in range(3):
        turn_left()
 
def forward():
    while not wall_in_front():
        move()
 
while(1):
    forward()
    if wall_in_front():
        turn_left()
        forward()