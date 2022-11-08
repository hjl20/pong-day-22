from turtle import Turtle

COLOR = "white"
SCREEN_HEIGHT = 250
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.goto(0, SCREEN_HEIGHT)
        self.p1_score = 0
        self.p2_score = 0
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.write(f"{self.p1_score}        {self.p2_score}", align=ALIGNMENT, font=FONT)

    def update_p1_score(self):
        self.p1_score += 1

    def update_p2_score(self):
        self.p2_score += 1
