from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")



screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey( fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down" )
screen.onkey(fun= snake.left, key="Left")
screen.onkey( fun= snake.right, key="Right")




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect collosion with food :

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#Detect collosion with walls :
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset_scoreboard()
        snake.reset()
#Detect collosion with tail :
    for segment in snake.segments[1:] :
        
        if snake.head.distance(segment) < 10 :
            scoreboard.reset_scoreboard()
            snake.reset()

        
   


screen.exitonclick()