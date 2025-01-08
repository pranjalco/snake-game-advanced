from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pranjal Sarnaik's Snake Game")


tim = Turtle()
tim.shape("square")
tim.color("white")

size = (tim.turtlesize())
width = 20 * size[0]
height = 20 * size[1]
print(f"{width} {height}")


















screen.exitonclick()
