from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 235)
        self.hideturtle()
        self.score = 1
        self.write("Score: " + str(self.score), move=False, align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write("Score: " + str(self.score), move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
