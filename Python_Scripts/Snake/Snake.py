import turtle as t

MOVE_DISTANCE=15
ALL_SNEK=[]
POSITIONS=[(0,0),(0,20),(0,40)]
class Snake:
    def __init__(self):
        self.create_snek()
        self.head=ALL_SNEK[0]
#Building the initial Snake
    def create_snek(self):
        for stuff in POSITIONS:
            self.make_snek(stuff)
#Setting up the snake properties
    def make_snek(self,position):
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.speed("slowest")
        snake.penup()
        snake.goto(position)
        ALL_SNEK.append(snake)
#Making the Snake longer
    def add_snek(self):
        self.make_snek(ALL_SNEK[-1].position())

#Movement Logic
    def move(self):
        for snek_num in range(len(ALL_SNEK) - 1, 0, -1):
            new_x = ALL_SNEK[snek_num - 1].xcor()
            new_y = ALL_SNEK[snek_num - 1].ycor()
            ALL_SNEK[snek_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)