from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game - LRV')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

difficulty_level = 0.1
difficulty_prompt = screen.textinput(title='Difficulty Levels:', prompt="What level you prefer?\n - Easy "
                                                                        "\n - Middle ""\n -Hard")
if difficulty_prompt and difficulty_prompt.lower() == 'easy':
    difficulty_level = 0.3
if difficulty_prompt and difficulty_prompt.lower() == 'middle':
    difficulty_level = 0.1
if difficulty_prompt and difficulty_prompt.lower() == 'hard':
    difficulty_level = 0.05

screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(difficulty_level)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()



    # Detect collision with tail
    # if head collides with any segment in the tail:
    # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()
