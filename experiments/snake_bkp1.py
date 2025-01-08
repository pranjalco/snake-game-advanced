# from turtle import Turtle, Screen
# import random
#
# STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
#
#
# class Snake:
#
#     def __init__(self):
#
#         self.segments = []
#         self.create_snake()
#
#     def create_snake(self):
#         for position in STARTING_POSITION:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#
#         self.segments[0].forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.segments[0].heading() == 0:
#             new_heading = self.segments[0].heading() + 90
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 90:
#             pass
#
#         elif self.segments[0].heading() == 180:
#             new_heading = self.segments[0].heading() + 270
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 270:
#             pass
#
#     def down(self):
#         if self.segments[0].heading() == 0:
#             new_heading = self.segments[0].heading() + 270
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 90:
#             pass
#
#         elif self.segments[0].heading() == 180:
#             new_heading = self.segments[0].heading() + 90
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 270:
#             pass
#
#     def left(self):
#         if self.segments[0].heading() == 0:
#             pass
#
#         elif self.segments[0].heading() == 90:
#             new_heading = self.segments[0].heading() + 90
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 180:
#             pass
#
#         elif self.segments[0].heading() == 270:
#             new_heading = self.segments[0].heading() + 270
#             self.segments[0].setheading(new_heading)
#
#     def right(self):
#         if self.segments[0].heading() == 0:
#             pass
#
#         elif self.segments[0].heading() == 90:
#             new_heading = self.segments[0].heading() + 270
#             self.segments[0].setheading(new_heading)
#
#         elif self.segments[0].heading() == 180:
#             pass
#
#         elif self.segments[0].heading() == 270:
#             new_heading = self.segments[0].heading() + 90
#             self.segments[0].setheading(new_heading)