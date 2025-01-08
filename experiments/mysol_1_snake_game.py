from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pranjal Sarnaik's Snake Game")

x_pose = 0
snake_parts = []
for _ in range(3):
    tim = Turtle("square")
    tim.color("white")
    tim.goto(x_pose, 0)
    snake_parts.append(tim)
    x_pose += -20

print(snake_parts)
















screen.exitonclick()
