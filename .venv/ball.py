from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('circle')
        self.shapesize(1.5)
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        if self.xcor() > 360 or self.xcor() < -360:
            self.goto(0, 0)
            self.bounce_x()
            self.move_speed = 0.1







