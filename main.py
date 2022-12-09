from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.015)
    screen.update()
    ball.move()

    #Collision with the top/bottom walls:
    if abs(ball.ycor()) >= 280:
        ball.bounce()

    #Collision with paddles:
    if abs(ball.xcor()) >= 340:
        if ball.distance(r_paddle) < 65 or ball.distance(l_paddle) < 65:
            ball.bounce_on_paddle()

    #Detect R paddle misses:
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()