"""
Udemy link : "https://www.udemy.com/course/mini-python-projects/" - Course Created by : Shambhavi Gupta
https://docs.python.org/3/library/turtle.html
turtle module - Using Turtle Graphics
TurtleScreen class defines graphics window for drawing turtles
RawTurtle defines Turtle objects which draw on the TurtleScreen
"""
import turtle                           #import turtle module

turtle.bgcolor("lightblue")             #Set or return bg colour of the TurtleScreen. Find colour hex (#) with use of colour picker from google, firefox etc.
turtle.pen(speed = 0.1)                   #a 'pen-dictionary' to set or return pen attributes
turtle.pensize(2.5)                     #Set line thickness (attributes could be assigned individually or within turtle.pen())
turtle.fillcolor("green")               #set the fill color - pencolor and fillcolor can be set together using color()

colours = ["red", "green", "orange", "yellow"]
for i in range(9):
    for c in colours:
        turtle.color(c)                 #assigning the turtle/pen colours
        turtle.circle(150)              #draw a circle with a given radius
        turtle.left(10)                 #turn tutrle left by angle units

#turtle testing
# turtle.color("black")
# turtle.forward(200)
# turtle.color("white")
# turtle.stamp()
# turtle.home()
# turtle.color("black")
# turtle.back(200)
# turtle.color("white")
# turtle.home()
# turtle.right(200)
# turtle.left(200)
# turtle.home()

turtle.mainloop()                       #starts event loop - calling Tkinter's mainloop function. Must be last statement in turtle graphics program.