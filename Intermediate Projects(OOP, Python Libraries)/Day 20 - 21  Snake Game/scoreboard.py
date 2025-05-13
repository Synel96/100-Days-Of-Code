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
        with open("data.txt", "r") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as data :
                data.write(f"{self.highscore}")

        
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} Highscore : {self.highscore}", align="center",font=FONT)






