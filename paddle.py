from turtle import Turtle
class Paddle(Turtle):
    def __init__(self , pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.goto(self.x_pos, self.y_pos )

    def up(self):
        self.y_pos += 20
        self.goto(self.x_pos, self.y_pos )
    def down(self):
        self.y_pos -= 20
        self.goto(self.x_pos, self.y_pos)