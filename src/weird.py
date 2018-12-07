import turtle
from math import sin


class CircleDrawer:
    def __init__(self, t):
        self.t = t
        self.t.pencolor("white")

    def draw(self, pos=(0, 0), angle=1., side=1., deformation_function=None):
        self.t.penup()
        self.t.setpos(pos)
        self.t.pendown()
        self.t.setheading(to_angle=0)

        for i in range(int(360 / angle)):
            if deformation_function:
                angle += deformation_function(i / 50.) / 3.
            self.t.forward(side)
            self.t.left(angle)
        turtle.update()


def main():
    t = turtle.Turtle()

    turtle.setup(width=1900, height=950)
    turtle.bgcolor("black")
    t.hideturtle()
    t.setheading(to_angle=0)
    turtle.tracer(0, 0)
    t.width(.5)

    circle_drawer = CircleDrawer(t)

    g = 100
    for i in range(g):
        circle_drawer.draw(angle=.009 + i / 3333., side=1.3,
                           deformation_function=lambda x: sin(x / 50.), pos=(-500 + i * 15, 150))

    turtle.exitonclick()


if __name__ == '__main__':
    main()



