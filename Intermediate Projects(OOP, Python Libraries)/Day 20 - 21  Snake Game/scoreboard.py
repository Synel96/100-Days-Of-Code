from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier",20,"normal")
class Scoreboard(Turtle) :

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.write(arg=f"Score : {self.score} ", align=ALIGMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score} ", align="center",font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align="center",font=FONT)




