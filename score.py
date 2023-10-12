from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.clear()

    def write_score(self,point):
        self.score += point
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))

    def winner(self,winner):
        self.clear()
        self.write("{} Wins!!".format(winner), align="center", font=("Courier", 24, "normal"))

