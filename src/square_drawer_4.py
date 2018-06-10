import turtle
import os
import glob
import random
import time
from math import sin, sqrt, cos

class Converter:
    def __init__(self):
        pass

    def ps_to_png(self, ps_file):
        root = ps_file[:-2]
        pngfile = root + 'png'
        os.system('convert ' + ps_file + ' ' + pngfile)


class SquareDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.setheading(to_angle=0)
        self.t.tracer(0, 0)
        self.t.width(1)

    def get_canvas(self):
        cv = turtle.getcanvas()
        return cv

    def save_canvas(self, canvas, filename="abc.ps"):
        canvas.postscript(file=filename, colormode='color')

    def draw(self, pos=(0, 0), n=4, side=20, rotation=0):
        self.t.penup()
        self.t.setpos(pos)
        self.t.setheading(rotation)
        self.t.pendown()

        self._draw_ngon(n=n, side=side)

    def _draw_ngon(self, n=4, side=20):
        for _ in range(n):
            self.t.forward(side)
            self.t.left(360./n)


class SequenceGenerator:
    def __init__(self):
        pass

    def get_grid(self, offset=(0, 0), rows=20, cols=20, step_v=5, step_h=5):
        for row in range(rows):
            for col in range(cols):
                yield offset[0] + col*step_v, offset[1] - row*step_h


def main():
    turtle.setup(width=1900, height=950)

    square_drawer = SquareDrawer()
    sequence_generator = SequenceGenerator()

    side = 60
    rows, cols = 45/3/2, 90/3/2
    step_h, step_v = side*2, side*2
    offset = -930, 440

    turtle.bgcolor("black")
    square_drawer.t.pencolor("white")

    func = lambda x: (sin(x) + sin(x/1.1)) / 2
    # func = lambda x: sin(x)

    for j in range(2000):
        square_drawer.t.clear()
        for i, (col, row) in enumerate(sequence_generator.get_grid(offset=offset,
                                                                   step_h=step_h, step_v=step_h,
                                                                   rows=rows, cols=cols)):

            what = (i)/float((j+1)/100.)

            sideee = side * abs(func(what))

            square_drawer.draw(n=5, pos=(col, row), side=sideee, rotation=func(j/10.)*36)

        turtle.update()

    turtle.exitonclick()


if __name__ == '__main__':
    main()
