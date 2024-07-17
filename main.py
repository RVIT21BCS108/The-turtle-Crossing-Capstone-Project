import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player() # to create a new turtle from turtle class
car_manager = CarManager() # to create a  new car
scoreboard = Scoreboard() # to create a scoreboard for each level

screen.listen()
screen.onkey(player.go_up, "Up") # to make turtle move up when up key pressed( by calling
# go_up function from player file)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # every 0.1 second screen refreshed

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars: # loop though all cars in the list
        if car.distance(player) < 20: # each car is 20 pixels high an 0 pixels wide so if
            # ditance between car and player less than 20 pixels they collided
            game_is_on = False # finish game by making False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line(): # if true returned (turtle cross finish line)
        player.go_to_start() # make it go to starting position
        car_manager.level_up() # increase car speed at next level
        scoreboard.increase_level()


screen.exitonclick()
