from turtle import Turtle


class Pad(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("#eee3de")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.penup()
        self.position_x = x_cor
        self.position_y = y_cor
        self.goto(self.position_x, self.position_y)

    def right_p(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.position_y)

    def left_p(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.position_y)
