from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.goto(0, -50)
        self.speed_multiplier = 1.21
        self.total_multiplier = 1
        self.x_move = 1
        self.y_move = 1

    def move(self, scr_edge_x:int, scr_edge_y:int):
        if self.xcor() > scr_edge_x or self.xcor() < -scr_edge_x:
            self.bounce_x()
        if self.ycor() > scr_edge_y:
            self.bounce_y()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, -70)
        self.x_move = 0
        self.y_move = -0.6
        self.total_multiplier = 1

    def increase_speed(self):
        if abs(self.y_move) < 5:
            self.x_move *= self.speed_multiplier
            self.y_move *= self.speed_multiplier
            self.total_multiplier *= self.speed_multiplier
