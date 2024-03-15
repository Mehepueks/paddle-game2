from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen = Screen()

screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
speed_x = 2
speed_y = 2

screen.listen()
#right paddle movements
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
#left paddle movements
screen.onkey(l_paddle.up, 'a')
screen.onkey(l_paddle.down, 'z')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed(+1)

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()