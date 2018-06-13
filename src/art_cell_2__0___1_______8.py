import turtle
import random

from classes import (ArtCell, Fullness, ProbabilityDistribution, Art_2__0___1_____8___i__m_a_g__e,
                     GridOfArtCells, __default_dimensions__, __default_position__)


def main():
    turtle.setup(width=1900, height=950)
    turtle.bgcolor("black")
    turtle.pencolor("white")

    t = turtle.Turtle()

    t.pensize(3)
    x_offset, y_offset = -900, -400
    x_spacing, y_spacing = 25, 25

    rows, cols = __default_dimensions__
    positions_xy = list(range(0, cols)), list(range(0, rows))
    art_cells = []

    t.clear()

    for y in positions_xy[1]:
        for x in positions_xy[0]:
            position = x*x_spacing + x_offset, y*y_spacing + y_offset
            cell = ArtCell(t=t, position=position, orientation=random.randint(0, 3))
            art_cells.append(cell)

    prob_dist = ProbabilityDistribution()
    art_grid = GridOfArtCells(t, art_cells, prob_dist=prob_dist)

    image = Art_2__0___1_____8___i__m_a_g__e(turtle=t, grid=art_grid)

    image.display()
    # image.t.clear()

    turtle.exitonclick()


if __name__ == '__main__':
    main()
