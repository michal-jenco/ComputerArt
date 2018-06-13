import turtle
import random
from math import sin, cos, sqrt

from classes import (ArtCell, Fullness, ProbabilityDistribution, Art_2__0___1_____8___i__m_a_g__e,
                     GridOfArtCells, __default_dimensions__, __default_position__)


def main():
    turtle.setup(width=1900, height=950)
    turtle.bgcolor("black")
    turtle.pencolor("white")

    t = turtle.Turtle()

    x_offset, y_offset = -900, -400
    x_spacing, y_spacing = 30, 30

    rows, cols = __default_dimensions__
    positions_xy = list(range(0, cols)), list(range(0, rows))
    art_cells = []

    t.clear()

    for y in positions_xy[1]:
        for x in positions_xy[0]:
            position = x*x_spacing + x_offset, y*y_spacing + y_offset
            cell = ArtCell(t=t, position=position, orientation=random.randint(0, 3))
            art_cells.append(cell)

    # circle y_offset
    # (cos(i / 15.) / 2. + 1) * 150, (sin(i / 15.) / 2. + 1) * 150)

    interesting_functions = {0: lambda x, y: ((sin(sin(x+i*sin(y-i**i))))+1)*2,
                             1: lambda x, y: min(sqrt(x)*i/(y+1), 3),
                             2: lambda x, y: max(min(sin(sin(y))*i/(y+1), 3), 0),
                             3: lambda x, y: int(random.randint(0, 3)),
                             4: lambda x, y: ((sin(x/(i+.001) + sin(y/(i+.001)/2.))+1)/.5)}

    del x, y
    for i in range(1000):
        print("Animation: %s" % i)
        prob_dist = ProbabilityDistribution(value_func=interesting_functions[4])
        art_grid = GridOfArtCells(t, art_cells, prob_dist=prob_dist)

        image = Art_2__0___1_____8___i__m_a_g__e(turtle=t, grid=art_grid)

        image.t.clear()
        image.display(offset=(0, 0))

    turtle.exitonclick()


if __name__ == '__main__':
    main()
