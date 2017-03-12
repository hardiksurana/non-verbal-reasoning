# import turtle
# turtle.setup(800, 600)
# alex = turtle.Turtle()
# alex.forward(300)
# alex.left(90)
# alex.forward(200)
# exit()


import turtle

turtle.setup(800, 600)      # set the window size to 800 by 600 pixels
wn = turtle.Screen()        # set wn to the window object
wn.bgcolor("lightgreen")    # set the window background color
wn.title("Hello, Tess!")    # set the window title

sq = [(0,0),(0,10),(10,0),(10,10)]

tess = turtle.Turtle()
tess.color("blue")           # make tess blue
tess.pensize(3)              # set the width of her pen

tess.forward(300)
tess.left(120)
tess.forward(300)

wn.exitonclick()