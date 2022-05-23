import turtle as t
import random
#import colorgram

#colors extraction method
#colors = colorgram.extract('image.jpg', 30)
#print(colors)
#rgbColors = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    newColor = (r, g, b)
#    rgbColors.append(newColor)
#print(rgbColors)

t.colormode(255)
tim = t.Turtle()
colorList = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
numberOfDots = 100

for dotCount in range(1, numberOfDots + 1):
    tim.dot(20, random.choice(colorList))
    tim.forward(50)
    if dotCount % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()