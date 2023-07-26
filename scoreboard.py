from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.Speedx = 0.2
        self.kont = True
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 18, "normal"))

    def increease_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))


    def speedx(self):

        if self.score == 0:
            return self.Speedx
            pass
        elif self.score % 5 == 0 and self.kont == True:
             self.Speedx = self.Speedx/1.2
             self.kont=False
             return self.Speedx

        elif self.score % 5 != 0:
            self.kont = True
            return self.Speedx
        else:
            return self.Speedx
