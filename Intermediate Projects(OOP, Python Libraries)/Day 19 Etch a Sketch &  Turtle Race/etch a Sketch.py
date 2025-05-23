from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear_screen():
    timmy.home()
    timmy.clear()
    



screen.listen()
screen.onkey(fun=move_forwards,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear_screen,key="c")
screen.exitonclick() 