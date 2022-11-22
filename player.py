from turtle import Turtle, Screen
STARTING_X = 0
STARTING_Y = -280
MOVE_DISTANCE = 10
STARTING_POSITION = (STARTING_X, STARTING_Y)
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white", "white")
        self.go_to_start()
        self.setheading(90)
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        