import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
game_loop = 0
cars = []

while game_is_on:
    # generate a car every 1sec
    if game_loop % 10 == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        # detect collision with the player and end game
        if car.distance(player) < 25:
            game_is_on = False

        car.move()
        # remove car after it has reached the other side
        if car.xcor() < -350:
            cars.remove(car)

    time.sleep(0.1)
    screen.update()
    game_loop += 1

screen.exitonclick()
