from turtle import Turtle , Screen
import turtle as t

import random
from colors import turtle_colors


timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepSkyBlue")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return timmy.color(r, g ,b)

#first challange : Write a square 

#for i in range(0,4):
 #   timmy.forward(100)
  #  timmy.right(90)

#second challenge : draw dashed line 50 times

#for i in range(0,15):
#    timmy.pendown()
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)

# third challange :

# counter = 3

# def shape(side):
#     turn_angle = 360 / side
#     for i in range(side):
#         timmy.forward(100)
#         timmy.right(turn_angle)
    
# for i in range (0,10):
    
#     shape(counter)
#     counter += 1
#     timmy.color(random.choice(turtle_colors))

#fourth challange : Random Walk

# timmy.pensize(20)
# timmy.speed(6)


# forward_backward = ["forward","backward"]
# horizontal_directions =["left","right"]
# motion = {
#     "forward" : timmy.forward,
#     "backward" : timmy.backward,
    
# }

# turn = {
#     "left" : timmy.left, 
#     "right":  timmy.right
# }

# for _ in range(random.randint(50,200)):
#     turn[random.choice(horizontal_directions)](90)
#     motion[random.choice(forward_backward)](30)
#     random_color()

#challange 5 : Spirograph with turtle

timmy.speed("fastest")
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy.circle(70)
#         timmy.left(size_of_gap)
#         random_color()

# draw_spirograph(5)


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
t.colormode(255)
timmy.penup()
timmy.goto(-200,-200)
timmy.pendown()
def row():
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        
def new_row() :    
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(360)

for _ in range (15):
    row()
    new_row()

screen = Screen()
screen.exitonclick()