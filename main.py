import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
screen.setup(width=1000, height=500)

userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the game. Select color: ").lower()


feliz = Turtle(shape="turtle")
feliz.color("green")


feliz2 = Turtle(shape="turtle")
feliz2.color("red")


feliz3 = Turtle(shape="turtle")
feliz3.color("yellow")


feliz4 = Turtle(shape="turtle")
feliz4.color("blue")


feliz5 = Turtle(shape="turtle")
feliz5.color("purple")

speed = [4,2,1,5,4,3,6,3,2,5]

def start():
    feliz.penup()
    feliz.goto(x=-450, y=200)

    feliz2.penup()
    feliz2.goto(x=-450, y=100)

    feliz3.penup()
    feliz3.goto(x=-450, y=0)

    feliz4.penup()
    feliz4.goto(x=-450, y=-100)

    feliz5.penup()
    feliz5.goto(x=-450, y=-200)


def race():
    feliz.forward(random.choice(speed))
    feliz2.forward(random.choice(speed))
    feliz3.forward(random.choice(speed))
    feliz4.forward(random.choice(speed))
    feliz5.forward(random.choice(speed))


def doit():
    done = False
    while not done:
        if feliz.xcor() < 400 and feliz2.xcor() < 400 and feliz3.xcor() < 400 and feliz4.xcor() < 400 and feliz5.xcor()< 400:
            race()

        else:

            if feliz.xcor() == 399:
                print(f"You won. Winning color is {feliz.pencolor()}")
                done = True
            elif feliz2.xcor() == 399:
                print(f"You won. Winning color is {feliz2.pencolor()}")
                done = True
            elif feliz3.xcor() == 399:
                print(f"You won. Winning color is {feliz3.pencolor()}")
                done = True
            elif feliz4.xcor() == 399:
                print(f"You won. Winning color is {feliz4.pencolor()}")
                done = True
            elif feliz5.xcor() == 399:
                print(f"You won. Winning color is {feliz5.pencolor()}")
                done = True


            else:
                print(f"You Lose. Winning color is")
                done= True



start()
doit()


















# diction={
#     "w":move_forwards(),
#     "s":move_backwards(),
#     "a":move_counter_clockwise(),
#     "d":move_clockwise()
# }
#
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()


