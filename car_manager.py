from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.shapesize(1, 2, 1)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.speed *= MOVE_INCREMENT
