#
#
import turtle


def boustrophedon(g):
    "'This function fills up the square in a bustrophedon pattern.'"
    #draws the inner filings
    g.penup()
    g.setpos(-170, 170)
    g.pendown()
    for w in range(45):
        g.color("yellow")
        g.speed(10)
        g.right(90)
        # side.forward(5)
        g.left(90)
        g.forward(440)
        g.right(90)
        g.forward(5)
        g.right(90)
        g.forward(440)
        g.left(90)
        g.forward(5)
        g.left(90)
def square (side):
    "'This function draws the square. '"
    # draw square
    for i in range(2):
        side.forward(500)
        side.right(90)
        side.forward(500)
        side.right(90)

def main():
    "'This is where the two functions come together. "''
    #Create a window
    wn = turtle.Screen()
    wn.bgcolor("white")
    #Create a turtle
    side = turtle.Turtle()
    side.penup()
    side.setpos(-200,200)
    side.pendown()
    side.pensize(30)
    #draw the insides
    square (side)
    boustrophedon (side)
    wn.exitonclick()

main()

