from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("purple")
        self.penup()
        self.x_move = 10
        self.y_move = 10



    def move_ball(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position, )

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

