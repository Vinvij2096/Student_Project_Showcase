#Importing required classes
from random import choice
from turtle import Screen
import time
from Snake import Snake, ALL_SNEK
from Food import Food
from Score import Score

#Setting up the interface
screen=Screen()
screen.setup(width=1200,height=1000)
screen.bgcolor("black")
screen.title("SNEK")
screen.tracer(0)
snek=Snake()
food=Food()
score=Score()
snek.head.setheading(choice([0,180,270]))

#Setting up the user interaction
screen.listen()
screen.onkey(snek.up,"Up")
screen.onkey(snek.down,"Down")
screen.onkey(snek.left,"Left")
screen.onkey(snek.right,"Right")
game_on = True

#The Looop
while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

#Collision Logic
    #To detect food
    if snek.head.distance(food)<15:
        food.move()
        score.increase()
        snek.add_snek()
    #To detect Wall
    if snek.head.xcor()>590 or snek.head.xcor()<-595 or snek.head.ycor()>495 or snek.head.ycor()<-490:
        score.game_over()
        game_on=False
    #To detect Tail
    for stuff in ALL_SNEK[1:]:
        if snek.head.distance(stuff)<10:
            score.game_over()
            game_on = False

screen.exitonclick()

