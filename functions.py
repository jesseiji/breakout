def check_paddle_bounce(paddle:object, ball:object):
    if abs(ball.ycor() - paddle.ycor()) <= 15 and abs(ball.xcor() - paddle.xcor()) < 80:
        if ball.x_move == 0:
            vary_bounce(ball, paddle, True)
        else:
            vary_bounce(ball, paddle, False)
        return True

def check_ball_out(ball:object, paddle:object, score:object):
    if ball.ycor() < float(paddle.ycor())-50:
        ball.reset()
        paddle.move_speed = 20
        score.decrease_hearts()
        return True

def vary_bounce(ball:object, paddle:object, first:bool):
    coords = [[-80, -52], [-52, -14], [-14, 14], [14, 52], [52, 80]]
    angles = [1.5, 1, 0.75, 1, 1.5]
    count = 0
    bounced = False

    for coord in coords:
        if paddle.xcor() + coord[0] <= ball.xcor() < paddle.xcor() + coord[1]:
            angle = angles[count]
            if first:
                ball.y_move = -1
                ball.x_move = angle
            else:
                if ball.x_move < 0:
                    ball.x_move = -angle * ball.total_multiplier
                else:
                    ball.x_move = angle * ball.total_multiplier

            bounced = True
            ball.increase_speed()
            paddle.increase_speed()
            break
        count += 1

    if bounced:
        ball.bounce_y()

def check_box_bounce(ball, boxes, score:object):
    score_increase = 800
    for box_g in boxes:
        for box in box_g:
            bounced0 = False
            if (ball.x_move > 0 and ball.xcor() < box.xcor()) or (ball.x_move < 0 and ball.xcor() > box.xcor()):
                if abs(ball.xcor() - box.xcor()) <= 46 and abs(ball.ycor() - box.ycor()) <= 15:
                    ball.bounce_x()
                    bounced0 = True
            if (ball.y_move > 0 and ball.ycor() < box.ycor()) or (ball.y_move < 0 and ball.ycor() > box.ycor()):
                if abs(ball.xcor() - box.xcor()) < 37 and abs(ball.ycor() - box.ycor()) <= 20:
                    ball.bounce_y()
                    bounced0 = True
            if bounced0 == True:
                box.clear()
                box.hideturtle()
                box_g.remove(box)
                score.increase_score(score=int(score_increase))
                break

        score_increase -= 200