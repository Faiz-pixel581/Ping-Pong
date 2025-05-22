from turtle import Turtle


class Paddle(Turtle): #inheriting
    def __init__(self, position):
        super().__init__()
        self.shape("square") #making one paddle
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5 units tall, 1 unit wide and it's a stretched square not multiple segments

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):    #  x is left to right and y is top to bottom
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)