from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.shapesize(1, 5)
        self.setposition(position)

    def up(self):
        if self.ycor() == 280:
            pass
        else:
            self.forward(20)

    def down(self):
        if self.ycor() == -280:
            pass
        else:
            self.backward(20)
