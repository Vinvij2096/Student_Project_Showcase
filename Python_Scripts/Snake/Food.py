from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()
#Randomising the food location
    def move(self):
        random_x = randint(-580, 580)
        random_y = randint(-480, 470)
        self.goto(x=random_x, y=random_y)