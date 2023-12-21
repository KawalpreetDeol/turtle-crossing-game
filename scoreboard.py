from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    score = 1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-220, 260)
        self.display_score()

    def display_score(self):
        self.write(f'Level: {str(self.score)}', False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=FONT)
    
    def increment_score(self):
        self.score+=1
        self.clear()
        self.display_score()
    
    def refresh_score(self):
        self.score = 1
        self.clear()
        self.display_score()