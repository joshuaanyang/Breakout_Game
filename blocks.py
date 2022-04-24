from turtle import Turtle
import random


COLORS = ["#F1DDBF", "#525E75", "#92BA92", "#DFDFDE"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.pos_x = -390
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def get_car(self):
        while self.pos_x < 390:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # new_car.setheading(180)
            new_car.goto(self.pos_x, 230)
            self.pos_x = self.pos_x + 43
            self.all_cars.append(new_car)

    def checking(self, player_x):
        for car in self.all_cars:
            if car.distance(player_x) < 30 and car.ycor()>200:
                car.reset()
                car.hideturtle()
                return True
