import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # check successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()


screen.exitonclick()
