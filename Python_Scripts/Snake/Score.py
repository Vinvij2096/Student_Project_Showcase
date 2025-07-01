from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 0
        self.color("white")
        with open("data.txt", "r") as high_score:
            self.high_score=int(high_score.read())
        self.goto(0, 470)
        self.update()
        self.hideturtle()

#Updating scoreboard
    def update(self):
        self.clear()
        self.write(arg=f"Score:{self.count} High Score:{self.high_score}", align="center", font=("Courier", 20, "normal"))
#Increasing score per food eaten
    def increase(self):
        self.count+=1
        if self.count>self.high_score:
            self.high_score = self.count
        self.update()

#Resetting the game
    def game_over(self):
        if self.count>=self.high_score:
            with open("data.txt", "w") as high_score:
                high_score.write(str(self.count))
        self.update()
        self.goto(0, 0)
        self.write(arg=f"Game Over!!\nYour Score was:{self.count}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()
        self.count = 0

