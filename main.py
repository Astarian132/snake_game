import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.setup(width=1250, height=650)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
score.show_score(snake.snake_lenght)
game_on = True
while game_on:
    snake.move()
    screen.update()
    # Speed adjustment
    time.sleep(0.05)


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.show_score(snake.snake_lenght)
        screen.update()

    #Detect collision with wall
    if abs(snake.head.xcor()) > 620 or abs(snake.head.ycor()) > 320:
        score.game_over()
        game_on = False

    #Detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
