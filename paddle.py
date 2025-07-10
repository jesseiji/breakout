from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos:tuple):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=8)
        self.pu()
        self.speed(0)
        self.goto(pos)
        self.move_speed = 20

    def move_r(self):
        if not self.xcor() + 8*10 + self.move_speed > 210:
            self.goto(self.xcor() + self.move_speed, self.ycor())
        else:
            self.goto(
                self.xcor() + (132.5-self.xcor()),
                self.ycor()
            )


    def move_l(self):
        if not self.xcor() - 8*10 - self.move_speed < -210:
            self.goto(self.xcor() - self.move_speed, self.ycor())
        else:
            self.goto(
                self.xcor() - (137.5+self.xcor()),
                self.ycor()
            )

    def increase_speed(self):
        if self.move_speed < 40:
            self.move_speed *= 1.2
