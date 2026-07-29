from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
speed = 0.1
r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))


screen = Screen()
screen.setup(800 , 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score_board = ScoreBoard()

ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.up , "Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up , "w")
screen.onkeypress(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if r_paddle.distance(ball) < 70 and ball.xcor() > 320 or l_paddle.distance(ball) < 70  and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.misses(r_paddle)
        score_board.l_point()
        if speed > 0.03:
            speed -= 0.01
        else:
            pass

    if ball.xcor() < -380:
        ball.misses(l_paddle)
        score_board.r_point()
        if speed > 0.03:
            speed -= 0.01
        else:
            pass


screen.exitonclick()