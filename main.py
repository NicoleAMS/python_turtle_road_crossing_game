import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
game_loop = 0

while game_is_on:
    # generate a car every 1sec
    if game_loop % 10 == 0:
        car_manager.create_car()

    for car in car_manager.cars:
        # detect collision with the player and end game
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

        # remove car after it has reached the other side
        if car.xcor() < -350:
            car_manager.cars.remove(car)

    if player.at_finish:
        car_manager.increase_speed()
        player.at_finish = False
        scoreboard.increase_level()

    car_manager.move()

    time.sleep(0.1)
    screen.update()
    game_loop += 1

screen.exitonclick()
