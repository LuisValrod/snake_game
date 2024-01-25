from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game - LRV')
screen.tracer(0)
snake = Snake()
food = Food()

difficulty_level = 0.1
# difficulty_prompt = screen.textinput(title='Difficulty Levels:', prompt="What level you prefer?\n - Easy "
#                                                                         "\n - Middle ""\n -Hard")
# if difficulty_prompt and difficulty_prompt.lower() == 'easy':
#     difficulty_level = 0.3
# if difficulty_prompt and difficulty_prompt.lower() == 'middle':
#     difficulty_level = 0.1
# if difficulty_prompt and difficulty_prompt.lower() == 'hard':
#     difficulty_level = 0.05

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


screen.exitonclick()
