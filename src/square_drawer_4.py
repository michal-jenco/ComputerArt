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

    for j in range(999999):
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
