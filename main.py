from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("yılan gamesi")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
print("")
games_true = True
while games_true:
    screen.update()
    time.sleep(score.speedx())
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.new_segment()
        score.increease_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        games_true = False
        score.gameover()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            games_true = False
            score.gameover()


screen.exitonclick()
