import turtle
import os
import glob
import random
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
        self.t.width(.2)

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

    def get_spiral(self, offset=(0, 0), steps=100, step_size=10, step_angle=5):
        for _ in range(steps):
            yield 0


def main():
    turtle.setup(width=1800, height=950)

    square_drawer = SquareDrawer()
    sequence_generator = SequenceGenerator()

    side = 1
    rows, cols = 260, int(120*4.21)
    step_h, step_v = side + 2, side + 5

    turtle.bgcolor("black")
    square_drawer.t.pencolor("white")

    side = 2
    offset = -880, 420
    smooth = 10.
    row_offset_mult, col_offset_mult = 10, 10

    for i in range(500):
        rows = 5
        cols = int(125)
        offset = -880, 420 - i*rows*3
        ___w_a__w_e___(cols, rows, sequence_generator, side, square_drawer, step_h, offset, smooth,
                       offset_mult=(row_offset_mult, col_offset_mult))

        turtle.update()

    turtle.exitonclick()


def ___w_a__w_e___(cols, rows, sequence_generator, side, square_drawer, step_h, offset, smooth, offset_mult):
    for i, (col, row) in enumerate(sequence_generator.get_grid(offset=offset,
                                                               step_h=step_h, step_v=step_h,
                                                               rows=rows, cols=cols)):
        rot = (cos(i / smooth) + 1) / 2
        rot *= 90
        rot = 0

        offset_base = (cos(i / smooth) + 1) / 2
        row_offset, col_offset = offset_base * offset_mult[0], offset_base * offset_mult[1]

        square_drawer.draw(n=1, side=side, pos=(col + row_offset, row + col_offset), rotation=rot)

        # if i % 1000 == 0:
        #     turtle.update()


if __name__ == '__main__':
    main()
