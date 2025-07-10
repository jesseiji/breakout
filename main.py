import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from boxes import Box
from score import Score

from functions import *
import time

screen = Screen()
screen.setup(450, 485)
# Remove
turtle.getcanvas().winfo_toplevel().geometry("+2700+200")

screen.title('Breakout Game')
screen.bgcolor('black')
screen.tracer(n=0)
edge_x = 210
edge_y = 170

score = Score()

edge_top = Turtle()
edge_top.color('white')
edge_top.shape('square')
edge_top.pu()
edge_top.goto(0, 190)
edge_top.shapesize(stretch_wid=0.25, stretch_len=22.5)

paddle = Paddle((0, -edge_y-30))
screen.onkey(paddle.move_r, 'Right')
screen.onkey(paddle.move_l, 'Left')
screen.listen()

ball = Ball()
ball.reset()
score.decrease_hearts()

colors = ['red', 'yellow', 'green', 'blue']
boxes = [[], [], [], []]
start_y = edge_y
for i in range(len(colors)):
    start_x = -180
    for _ in range(5):
        box = Box(color=colors[i], pos=(start_x, start_y))
        start_x += 87.5
        boxes[i].append(box)
    start_y -= 35

game_over = False
reset = True
count = 0
while not game_over:
    screen.update()

    ball.move(edge_x, edge_y)

    check_box_bounce(ball, boxes, score)

    if check_paddle_bounce(paddle, ball):
        reset = False

    if check_ball_out(ball, paddle, score):
        reset = True

    if score.is_game_over:
        game_over = True
        if score.score == -9999:
            if count < 16999:
                for box_g in boxes:
                    for box in box_g:
                        box.go_bottom()
                        count += 1
                        game_over = False
            else:
                game_over = True
        ball.goto(-9999, 0)
        paddle.goto(-9999, 0)


    time.sleep(0.011)

screen.update()
screen.exitonclick()