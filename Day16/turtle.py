import turtle
#from turtle import Turtle
#timmy = Turtle()

timmy = turtle.Turtle()
#Methods
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)
my_screen = turtle.Screen()

#ATTRIBUTES
print(my_screen.canvheight)
my_screen.exitonclick()