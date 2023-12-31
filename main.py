import random
import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
# screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()

screen_speed = 0.08

paddle_left = Paddle()
score_pd_left = Score()
score_pd_left.goto(-300, 200)
score_pd_right = Score()
score_pd_right.goto(200, 200)

winner_real_time = Score()
winner_real_time.goto(0,260)

paddle_right = Paddle()
paddle_left.goto(-250,-200)
paddle_right.goto(250,200)
balls = Ball()

screen.onkeypress(fun=paddle_left.go_up, key="w")
screen.onkeypress(fun=paddle_left.go_down, key="s")
screen.onkeypress(fun=paddle_right.go_up, key="Up")
screen.onkeypress(fun=paddle_right.go_down, key="Down")
score_pd_left.write_score(0)
score_pd_right.write_score(0)

game_is_on = True
while game_is_on:
    balls.moving()
    if balls.ycor() < -260:
        balls.yspeed *= -1
    elif balls.ycor() > 260:
        balls.yspeed *= -1

    if balls.xcor() == -250 and paddle_left.ycor()-50 <= balls.ycor() <= paddle_left.ycor()+50:
        balls.xspeed *= -1
        screen_speed -= 0.002
        score_pd_left.write_score(10)
    if balls.xcor() == 250 and paddle_right.ycor()-50 <= balls.ycor() <= paddle_right.ycor()+50:
        balls.xspeed *= -1
        score_pd_right.write_score(10)
        screen_speed -= 0.002

    if score_pd_right.score > score_pd_left.score:
        winner_real_time.winner('Right')
    else:
        winner_real_time.winner('Left')

    if balls.xcor() < -400 or balls.xcor() > 400:
        balls.ball_center()
        # game_is_on = False
        if score_pd_right.score > score_pd_left.score:
            winner_real_time.winner('Game over,Right')
        else:
            winner_real_time.winner('Game over,Left')

    time.sleep(screen_speed)
    screen.update()


screen.exitonclick()


