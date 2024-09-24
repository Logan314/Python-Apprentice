
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina


tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0) 
tina.penup()           

               # Make the turtle move as fast, but not too fast.

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))
colors = ["red", "blue", "green", "yellow", "orange"]



tina.goto(50,-100)
tina.pendown()
tina.pencolor('red') 
for i in range(20000):
    tina.left(89)
    tina.forward(i/-12)
    

turtle.exitonclick()
... # Your code here
