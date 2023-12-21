from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_player()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_player(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
