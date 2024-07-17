from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle): # import all attributes and methods of turtle class

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)  # make face north

    def go_up(self):
        self.forward(MOVE_DISTANCE) # move by certain distance when UP key clicked by user

    def go_to_start(self):
        self.goto(STARTING_POSITION)  # initially place turtle at this position when game begins

    def is_at_finish_line(self): # return true if turtle cross finish line else false
        if self.ycor() > FINISH_LINE_Y: # screen height is 600 ie -300 to +300  so when turtle y cord cross 280
            # crosses finish line
            return True
        else:
            return False
