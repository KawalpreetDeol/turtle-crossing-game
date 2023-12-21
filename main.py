import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
counter = 0
level = 0
while game_is_on:
    counter += 1
    if not counter % 1:
        car_manager.move_cars()
    # if not counter % 15/(1+level/10): # to generate cars 
    if not counter % 6: # to generate cars 
        car_manager.generate_cars()
        car_manager.delete_cars()
    time.sleep(0.1)

    for car in car_manager.cars:
        if player.distance(car) <= 30 and player.ycor() <= car.ycor() + 20 and player.ycor() >= car.ycor() - 20 :
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() > 280:
        player.reset_player()
        level+=1
        scoreboard.increment_score()
        car_manager.level_up()

    screen.update()

screen.exitonclick()
