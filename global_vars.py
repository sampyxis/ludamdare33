# not sure if this is the correct way to go about it...

def init():
    # Define some colors
    global BLACK
    global WHITE
    global RED
    global BLUE
    global BROWN
    global DARKGREY
    global GREY
    global PINK
    global OPEN_DOOR

    global player_size
    global player_color
    global player_direction

    global up
    global down
    global left
    global right

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (117, 124, 135)
    BROWN = (127, 51, 0)
    DARKGREY = (48,48,48)
    PINK = (255,0,110)
    OPEN_DOOR = (86,34,0)

    player_size = [16,16]
    player_color = RED

    player_direction = 0

    up = 0
    down = 1
    left = 2
    right = 3
