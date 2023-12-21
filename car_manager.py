from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class CarManager:
    cars = []
    level = 0
    max_cars = int((SCREEN_HEIGHT - 100) / 25 * 0.2) # Cannot have too many cars, otherwise impossible to cross
    def __init__(self):
        self.generate_cars()
        for i in range(int(SCREEN_WIDTH / 20)):
            self.move_cars()
    
    def build_car(self):
        car = Turtle("square")
        car.hideturtle()
        car.penup()
        car.turtlesize(stretch_len=2, stretch_wid=1)
        car.color(COLORS[random.randint(0,5)])
        car.setheading(180)
        car.goto(SCREEN_WIDTH/2, random.randint(-1*SCREEN_HEIGHT/2 + 60, SCREEN_HEIGHT/2 - 60))
        car.showturtle()
        return car

    def generate_cars(self):
        num_cars = 1 #random.randint(0, self.max_cars)

        for _ in range(num_cars):
            self.cars.append(self.build_car())

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level)
    
    def level_up(self):
        self.level+=1

    def delete_cars(self):
        trash_cars = []
        for i, car in enumerate(self.cars):
            if not (car.xcor() + 30 < -1*SCREEN_WIDTH/2): # only the first couple cars in the list will be crossing the finishing line
                break 
            trash_cars.append(i)

        for i in trash_cars[::-1]:
            trash_car = self.cars.pop(i)
            del(trash_car)
