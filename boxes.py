from turtle import Turtle
import random

class Box(Turtle):

    def __init__(self, color:str, pos:tuple):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3.6)
        self.pu()
        self.goto(pos)
        self.n = random.choice([0.5, 0.75, 1, 1.25, 1.5, 1.75])

    def go_bottom(self):
        self.goto(self.xcor(), self.ycor()-(self.n))