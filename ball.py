from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('circle')
        self.yspeed = -10
        self.xspeed = 10

    def moving(self):
        self.goto(self.xcor()+self.xspeed,self.ycor()+self.yspeed)

    def ball_stop(self):
        self.goto(0,0)
