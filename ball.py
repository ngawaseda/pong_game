import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_velocity = 3
        self.x_velocity = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_velocity *= -1

    def bounce_on_paddle(self):
        self.x_velocity *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_on_paddle()
