from turtle import *
from pad import Pad
from ball import Ball
from blocks import CarManager
import time

screen = Screen()
screen.bgcolor("#222123")
screen.title("JoshPy Break the 4th Wall")
screen.setup(width=800, height=600)
screen.tracer(0)

turtle = Turtle()
turtle.hideturtle()
pad = Pad(0, -200)
ball = Ball()
block = CarManager()

screen.listen()
screen.onkey(pad.right_p, "Right")
screen.onkey(pad.left_p, "Left")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    block.get_car()

    if ball.ycor() == 290:
        ball.bounce_y()

    if ball.xcor() == 390 or ball.xcor() == -390:
        ball.bounce_x()

    if ball.distance(pad) < 50 and ball.ycor() < -198:
        ball.bounce_y()

    if block.checking(ball):
        ball.bounce_y()

    if ball.ycor() <= -290:
        game_is_on = False


turtle.color("#eee3de")
turtle.write("Game Over", move=False, align="center", font=("Arial", 34, "normal"))


screen.exitonclick()
