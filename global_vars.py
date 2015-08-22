# not sure if this is the correct way to go about it...

def init():
    # Define some colors
    global BLACK
    global WHITE
    global RED
    global BLUE
    global BROWN
    global GREY

    global player_size
    global player_color

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (117, 124, 135)

    player_size = [20,20]
    player_color = RED
