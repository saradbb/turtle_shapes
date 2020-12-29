
#Beautiful to Ugly
#This program lets users choose weather to make polygons, Random walk or spirograph
from turtle import Turtle, Screen
import random
import easygui

cool_turtle = Turtle()
cool_turtle.shape("turtle")
COLOR_NAMES = [
  "dark cyan",
    "maroon",
    "olive drab",
    "royal blue",
    "aquamarine",
    "aquamarine",
    "dark goldenrod",
    "maroon",
    "magenta",
    "red",
    "gold",
    "yellow",
    "navy",
    "medium slate blue",
    "lemon chiffon",
    "orange red",
"deep pink"
];

choice = int(easygui.enterbox("Ploygons: Press 1, Random Walk: Press 2, Spirograph: Press 3"))
screen = Screen()
screen.bgcolor("black")


def sidedFigures():
    """
    This function asks user for the # of sides of highest sided polygan and starting from triangle draws every polygon till that number.
    :return:
    """
    upper = int(easygui.enterbox("How many sided figure do  you want to see(3-15)?")) + 1

    for num in range(3,upper):
        color = random.choice(COLOR_NAMES)
        cool_turtle.pencolor(color)
        angle = 360/num
        for i in range(0,num):
            cool_turtle.forward(100)
            cool_turtle.right(angle)

def randomWalk():
    """
    This function draws a random walk on the screen.
    :return:
    """
    walk_num = random.randint(45,70)
    for _ in range(0,walk_num):
        color = random.choice(COLOR_NAMES)
        steps = random.randint(10,95)
        angle = random.randint(0,360)
        cool_turtle.pencolor(color)
        cool_turtle.right(angle)
        cool_turtle.forward(steps)

def draw_spirograph():
    """
    This function draws spinograph
    :return:
    """
    screen.bgcolor("white")
    cool_turtle.speed(0)
    for _ in range (0, 72):
        color = random.choice(COLOR_NAMES)
        cool_turtle.pencolor(color)
        cool_turtle.circle(60)
        cool_turtle.setheading(cool_turtle.heading()+5)
        cool_turtle.circle(60)

if choice == 1:
    sidedFigures()
elif choice == 2:
    randomWalk()
elif choice == 3:
    draw_spirograph()
else:
    easygui.msgbox('Please Enter a valid response', 'Invalid Input')

screen.exitonclick()

