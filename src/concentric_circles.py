from classes import CircleDrawer
import turtle
from math import sin


def main():
    t = turtle.Turtle()

    turtle.setup(width=1900, height=950)
    turtle.bgcolor("black")
    t.hideturtle()
    t.setheading(to_angle=0)
    t.tracer(0, 0)
    t.width(.5)

    circle_drawer = CircleDrawer(t)

    g = 100
    for i in range(g):
        circle_drawer.draw(angle=.004+i/1000., side=1.3, deformation_function=lambda x: sin(x/50), pos=(-500+i*15, 150))

    turtle.exitonclick()


if __name__ == '__main__':
    main()
