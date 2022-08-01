from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()

tim.shape("turtle")
tim.color("red")
tim.speed(9)
tim.width(9)
colormode(255)

tim.forward(30)
for _ in range(300):
    random_move = randint(1, 4)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    if random_move == 1:
        tim.right(90)
        tim.forward(30)
    elif random_move == 2:
        tim.left(90)
        tim.forward(30)
    elif random_move == 3:
        tim.left(180)
        tim.forward(30)
    elif random_move == 4:
        tim.forward(30)


screen = Screen()
screen.exitonclick()
