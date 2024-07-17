from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = [] # starting list empty
        self.car_speed = STARTING_MOVE_DISTANCE # set starting speed of car at game beginning as initial moving
        # distance

    def create_car(self):
        random_chance = random.randint(1, 6) # too many cars created every 0.1 second
        # so every time random_choice is 1 then only a car is created reducing number of cars
        # created allowing turtle to cross easily
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250) # cars created along y-axis screen width 600
            # so -300 to 300 cars created -250 to +250 allowing turtle some space to start an
            # end race
            new_car.goto(300, random_y) # cars created at extreme right end of screen
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed) # every new car created move forward

    def level_up(self):
        self.car_speed += MOVE_INCREMENT # when turtle cross finish line and go to next level increase car
        # speed by 10 each time
