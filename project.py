import turtle


def main():
    "'This makes the square and the window."''
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgcolor("white")
    side = turtle.Turtle()
    side.penup()
    side.setpos(-200,200)
    side.pendown()
    side.pensize(30)
    for i in range(2):
        side.forward(500)
        side.right(90)
        side.forward(500)
        side.right(90)
    wn.exitonclick()


main()

