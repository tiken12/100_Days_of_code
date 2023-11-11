# from turtle import Turtle, Screen
# from random import randint
# import random
# import turtle


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# # number_of_colors = 10
# # colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(9)])
# #              for i in range(number_of_colors)]
# # directions = [0, 90, 180, 270]
# # timmy_the_turtle.pensize(2)
# timmy_the_turtle.speed("fast")


# #Sphere circle
# for _ in range(38):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.circle(100)
#     current_heading = timmy_the_turtle.heading()
#     timmy_the_turtle.setheading(current_heading + 10)
# # #Random walk
# # for _ in range(200):
# #     timmy_the_turtle.color(random_color())
# #     timmy_the_turtle.forward(30)
# #     timmy_the_turtle.setheading(random.choice(directions))

# #  #Shape drawing shorter version
# # def draw_shape(num_sides):
# #    angle = 360 /num_sides
# #    for _ in range(num_sides):
# #       timmy_the_turtle.forward(100)
# #       timmy_the_turtle.right(angle)

# # for shape in range(3,11):
# #    timmy_the_turtle.color(random.choice(colors))
# #    draw_shape(shape)

#  #shape Drawing
# # def random_color():
# #     rgbl=[255,0,0]
# #     random.shuffle(rgbl)
# #     return tuple(rgbl)
# # #Drawing a triangle 360/3
# # for _ in range(3):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(120)
# # #Drawing a squre 360/4
# # for _ in range(4):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(90)
# # for _ in range(5):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(72)
# # for _ in range(6):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(60)
# # for _ in range(7):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(51.43)
# # for _ in range(8):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(45)
# # for _ in range(9):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(40)
# # for _ in range(10):
# #    timmy_the_turtle.forward(100)
# #    timmy_the_turtle.right(36)



#    # timmy_the_turtle.penup()
#    # timmy_the_turtle.forward(10)
#    # timmy_the_turtle.pendown()
   
#    # timmy_the_turtle.right(90)


# screen = Screen()
# screen.exitonclick()


#Hirst Painting
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day-18 Drawing\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 
19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots =100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()