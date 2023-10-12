from turtle import Turtle

BOTTOM = 270
UP = 90
LEFT = 180
RIGHT = 360
PADDLE_MOVE = 100
class Paddle(Turtle):
    def __init__(self):
       super().__init__()
       self.pu()
       self.shape('square')
       self.shapesize(stretch_len=1,stretch_wid=5)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(),self.ycor()+PADDLE_MOVE)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE)
